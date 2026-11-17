// Wind Tunnel Digital Dashboard - Arduino Firmware (L298N + MPXV7002DP)
const int PRESSURE_PIN = A0;
const int ENA_PIN = 9;              // PWM speed control (to L298N ENA)
const int IN1_PIN = 7;              // Direction pin 1 (to L298N IN1)
const int IN2_PIN = 8;              // Direction pin 2 (to L298N IN2)

const float ADC_MAX = 1023.0;
const int OVERSAMPLE = 64;
const int ZERO_SAMPLES = 200;
const unsigned long SAMPLE_INTERVAL_MS = 20;

float zeroOffsetPa = 0.0;
unsigned long nextSample = 0;
int currentFanPWM = 0;

float readPressureRatio() {
  unsigned long sum = 0;
  for (int i = 0; i < OVERSAMPLE; i++) sum += analogRead(PRESSURE_PIN);
  return (sum / (float)OVERSAMPLE) / ADC_MAX;
}

float ratioToPa(float ratio) {
  return (ratio - 0.5) / 0.0002;
}

void measureZero(float &mean, float &sd) {
  float sum = 0, sumSq = 0;
  for (int i = 0; i < ZERO_SAMPLES; i++) {
    float p = ratioToPa(readPressureRatio());
    sum += p;
    sumSq += p * p;
  }
  mean = sum / ZERO_SAMPLES;
  sd = sqrt(max(sumSq / ZERO_SAMPLES - mean * mean, 0.0f));
}

void setup() {
  Serial.begin(115200);
  pinMode(ENA_PIN, OUTPUT);
  pinMode(IN1_PIN, OUTPUT);
  pinMode(IN2_PIN, OUTPUT);
  
  // Set constant forward direction for the fan
  digitalWrite(IN1_PIN, HIGH);
  digitalWrite(IN2_PIN, LOW);
  analogWrite(ENA_PIN, 0); // Start with fan off

  delay(1000);
  float sd;
  measureZero(zeroOffsetPa, sd);
  Serial.print("# Zero offset (Pa): ");
  Serial.println(zeroOffsetPa, 2);
  Serial.print("# Zero noise std (Pa): ");
  Serial.println(sd, 2);
  Serial.println("Time(ms),Pressure(Pa),FanPWM");
  nextSample = millis();
}

void loop() {
  // 1. Handle incoming serial commands from your HTML browser dashboard
  if (Serial.available() > 0) {
    String incoming = Serial.readStringUntil('\n');
    incoming.trim();
    if (incoming.length() > 0) {
      if (incoming == "c") {
        float m, sd;
        measureZero(m, sd);
        zeroOffsetPa = m;
        Serial.print("# Re-zeroed. Offset (Pa): ");
        Serial.println(zeroOffsetPa, 2);
      } 
      else if (incoming.startsWith("S")) {
        int val = incoming.substring(1).toInt();
        currentFanPWM = constrain(val, 0, 255);
        
        // Apply PWM speed to L298N ENA pin
        analogWrite(ENA_PIN, currentFanPWM);
        
        Serial.print("# Fan PWM set to: ");
        Serial.println(currentFanPWM);
      }
    }
  }

  // 2. Stream data at regular intervals
  unsigned long now = millis();
  if ((long)(now - nextSample) >= 0) {
    nextSample += SAMPLE_INTERVAL_MS;
    float p = ratioToPa(readPressureRatio()) - zeroOffsetPa;
    
    Serial.print(now);
    Serial.print(",");
    Serial.print(p, 2);
    Serial.print(",");
    Serial.println(currentFanPWM);
  }
}
