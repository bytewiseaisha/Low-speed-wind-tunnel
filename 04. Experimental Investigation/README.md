# 04. Experimental Investigation

Pressure measurements in the physical tunnel, with PWM fan control and browser-based logging. This is the validation step for the analytical and CFD models.

## Files

| File | Description |
|---|---|
| `data_acquisition.ino` | Arduino firmware: sensor reading, zeroing, fan PWM, serial streaming |
| `logger.html` | Browser dashboard: connect, control fan, re-zero, log and download CSV |
| `Run_01.csv` | Experimental run 1 (9,262 samples, ≈ 343 s) |
| `Run_02.csv` | Experimental run 2 (13,076 samples, ≈ 261 s), tubes swapped |
| `Experimental_Images/` | Build and test photos |

## Hardware

| Component | Role |
|---|---|
| Arduino Uno | Data acquisition and fan control |
| MPXV7002DP (±2 kPa) | Differential pressure between Pitot and wall tap |
| Pitot tube + wall static tap | Stagnation and static pressure in the test section |
| L298N | PWM speed control for the fan (ENA = pin 9, IN1 = 7, IN2 = 8) |
| 12 V DC axial fan (≈ 2.5 A) | Drives the flow |

Sensor output → A0. Fan direction is fixed (IN1 high, IN2 low).

## Firmware

- 64× oversampling per reported sample
- Pressure from the sensor transfer function: `P (Pa) = (ratio − 0.5) / 0.0002`
- Zero offset measured at start-up from 200 samples (fan off) and subtracted from every reading
- Streams `Time(ms),Pressure(Pa),FanPWM` at 115200 baud every 20 ms (≈ 50 Hz)
- Serial commands: `c` re-zeroes the sensor, `S<0–255>` sets the fan PWM

The firmware was first prototyped in the Wokwi Arduino simulator before running on hardware.

## Dashboard (`logger.html`)

Open the file in **Chrome or Edge**, which support the Web Serial API.

1. Upload `data_acquisition.ino` to the Arduino.
2. Open `logger.html` and click **Connect Arduino**, then select the port.
3. Use the slider to set fan PWM (0 – 255). **Re-Zero Sensor** re-measures the offset.
4. Click **Stop & Download CSV** to stop the fan and save the session.

## Procedure

1. Run the fan for a while to let its speed and temperature settle.
2. Power the Arduino with the fan off so it measures the zero offset with no flow.
3. Check the live reading is stable near zero.
4. Step the fan through PWM ≈ 0, 50, 100, 150, 200 and 255, holding each setting.

## Data format

```
Time_ms,Pressure_Pa,FanPWM
```

A few rows at the start of each file are stale buffered values from before the Arduino reset.

## Results

| PWM band | Run 1 mean (Pa) | Run 2 mean (Pa) |
|---|---|---|
| 0 | +0.21 | −0.21 |
| 1 – 50 | +0.40 | −0.25 |
| 51 – 100 | +0.51 | −0.29 |
| 101 – 150 | +0.77 | −0.47 |
| 151 – 200 | +0.98 | −0.70 |
| 201 – 255 | +1.03 | −0.79 |

- Both runs show a steady rise in pressure magnitude with fan speed, so the measurement chain detects the flow.
- The signs are opposite because the Pitot and static tubes were connected the other way round in Run 2. **Analyse the runs separately or correct the sign before combining them.**
- The peak signal of ≈ 1 Pa corresponds to ≈ 1.2 m/s. This is smaller than one ADC step (≈ 4.9 Pa) and is resolved only through oversampling.

## Limitations

- The flow stayed well below the 5 m/s minimum of the models, so validation could not be completed. The likely causes are the fan's pressure capability, the L298N voltage drop and ≈ 2 A current limit, and leakage at the joints.
- The sensor's ±2 kPa range is far too wide for a ~1 Pa signal.
- The sensor was zeroed but not calibrated against a reference pressure, and velocity was not measured independently.
