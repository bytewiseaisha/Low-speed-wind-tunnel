// Wind Tunnel DAQ, MPXV7002DP
// Wiring: VS -> 5V, GND -> GND, OUT -> A0 (through RC filter)
// Pitot total pressure -> P1 port, static -> vacuum port
// Commands: 'c' = zero now, 'z' = report zero drift (does not change offset)
// Lines starting with # are comments for MATLAB to ignore

const int SENSOR_PIN = A0;
const float ADC_MAX = 1023.0;
const int OVERSAMPLE = 64;
const int ZERO_SAMPLES = 200;
const unsigned long SAMPLE_INTERVAL_MS = 20;

float zeroOffsetPa = 0.0;
unsigned long nextSample = 0;

float readRatio() {
  // Sensor and ADC share the 5V rail, so the ratio is independent of supply value
  unsigned long sum = 0;
  for (int i = 0; i < OVERSAMPLE; i++) sum += analogRead(SENSOR_PIN);
  return (sum / (float)OVERSAMPLE) / ADC_MAX;
}

float ratioToPa(float ratio) {
  return (ratio - 0.5) / 0.0002;
}

void measureZero(float &mean, float &sd) {
  float sum = 0, sumSq = 0;
  for (int i = 0; i < ZERO_SAMPLES; i++) {
    float p = ratioToPa(readRatio());
    sum += p;
    sumSq += p * p;
  }
  mean = sum / ZERO_SAMPLES;
  sd = sqrt(max(sumSq / ZERO_SAMPLES - mean * mean, 0.0f));
}

void setup() {
  Serial.begin(115200);
  Serial.println("# Fan OFF. Auto-zeroing in 3 s...");
  delay(3000);
  float sd;
  measureZero(zeroOffsetPa, sd);
  Serial.print("# Zero offset (Pa): ");
  Serial.println(zeroOffsetPa, 2);
  Serial.print("# Zero noise std (Pa): ");
  Serial.println(sd, 2);
  Serial.println("Time(ms),Pressure(Pa)");
  nextSample = millis();
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    float m, sd;
    if (c == 'c') {
      measureZero(m, sd);
      zeroOffsetPa = m;
      Serial.print("# Re-zeroed. Offset (Pa): ");
      Serial.println(zeroOffsetPa, 2);
      nextSample = millis();
    } else if (c == 'z') {
      measureZero(m, sd);
      Serial.print("# Zero drift (Pa): ");
      Serial.println(m - zeroOffsetPa, 2);
      nextSample = millis();
    }
  }

  unsigned long now = millis();
  if ((long)(now - nextSample) >= 0) {
    nextSample += SAMPLE_INTERVAL_MS;
    float p = ratioToPa(readRatio()) - zeroOffsetPa;
    Serial.print(now);
    Serial.print(",");
    Serial.println(p, 2);
  }
}