# 04. Experimental Investigation

Pressure measurements in the physical tunnel, with PWM fan control and browser-based logging. This is the validation step for the analytical and CFD models.

## Files

| File | Description |
|---|---|
| `arduino_data_acquisition.ino` | Arduino firmware: sensor reading, zeroing, fan PWM, serial streaming |
| `web_logger.html` | Browser dashboard: connect, control fan, re-zero, log and download CSV |
| `Experimental Results/wind_tunnel_test_1.csv` | Run 1, 9 V battery (9,262 samples, ≈ 343 s) |
| `Experimental Results/wind_tunnel_test_2.csv` | Run 2, 9 V battery (13,076 samples, ≈ 261 s), tubes swapped |
| `Experimental Results/wind_tunnel_test_3_liion.csv` | Run 3, 11.1 V Li-ion pack (19,864 samples, ≈ 397 s) |
| `Images/` | Build and test photos, including the Li-ion supply (`liion_power_setup.jpg`) |

## Hardware

| Component | Role |
|---|---|
| Arduino Uno | Data acquisition and fan control, powered over USB |
| MPXV7002DP (±2 kPa) | Differential pressure between Pitot and wall tap |
| Pitot tube + wall static tap | Stagnation and static pressure in the test section |
| L298N | PWM speed control for the fan (ENA = pin 9, IN1 = 7, IN2 = 8) |
| 12 V DC axial fan (≈ 2.5 A, ≈ 30 W) | Drives the flow |
| 9 V battery (Runs 1–2), then 3 × 18650 Li-ion, 11.1 V (Run 3) | Shared supply for the fan and the L298N |

Sensor output → A0. Fan direction is fixed (IN1 high, IN2 low).

## Firmware

- 64× oversampling per reported sample
- Pressure from the sensor transfer function: `P (Pa) = (ratio − 0.5) / 0.0002`
- Zero offset measured at start-up from 200 samples (fan off) and subtracted from every reading
- Streams `Time(ms),Pressure(Pa),FanPWM` at 115200 baud every 20 ms (≈ 50 Hz)
- Serial commands: `c` re-zeroes the sensor, `S<0–255>` sets the fan PWM

The firmware was first prototyped in the Wokwi Arduino simulator, with a custom MPXV7002DP model, before running on hardware.

## Dashboard (`web_logger.html`)

Open the file in **Chrome or Edge**, which support the Web Serial API.

1. Upload `arduino_data_acquisition.ino` to the Arduino.
2. Open `web_logger.html` and click **Connect Arduino**, then select the port.
3. Use the slider to set fan PWM (0 – 255). **Re-Zero Sensor** re-measures the offset.
4. Click **Stop & Download CSV** to stop the fan and save the session.

## Procedure

1. Connect the Pitot tube to port P1 and the wall tap to port P2, and keep them fixed. Check that the reading rises when the fan starts.
2. Warm the fan up at PWM 150 for 2–3 minutes, then stop it.
3. With the fan fully stopped, re-zero the sensor and check the live reading is stable near zero.
4. Hold the fan for about 60 s at each setting (Run 3: 255, 200, 150, 100, 50, 0), ending with a fan-off reading for drift correction.

Runs 1 and 2 used an earlier version of this procedure, and their tubes were connected in opposite directions.

## Data format

```
Time_ms,Pressure_Pa,FanPWM
```

A few rows at the start of each file are stale buffered values from before the Arduino reset.

## Results

### Initial runs (9 V battery)

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
- The peak signal of ≈ 1 Pa corresponds to ≈ 1.2 m/s. This pointed to the supply: a fan rated 12 V, ≈ 2.5 A (≈ 30 W) cannot run properly from a small 9 V battery, which sags heavily above a few hundred milliamps.

### Re-run (11.1 V Li-ion pack)

The 9 V battery was replaced with three 18650 Li-ion cells in series (11.1 V nominal), which can deliver several amps. The pack measured 11.82 V with the fan off and 11.66 V at full PWM, so it held its voltage under load.

| PWM | Battery voltage (V) | Pressure (Pa) | Velocity (m/s) |
|---|---|---|---|
| 255 | 11.66 | 3.80 | 2.49 |
| 200 | 11.68 | 3.68 | 2.45 |
| 150 | 11.70 | 2.26 | 1.92 |
| 100 | 11.73 | 1.15 | 1.37 |
| 50 | 11.76 | 0.29 | 0.69 |
| 0 | 11.82 | 0.00 | 0.00 |

Pressures are steady means corrected by the fan-off reading at the end of the run (0.76 Pa); velocities use V = √(2Δp/ρ).

- The peak signal rose about 3.7 times, to ≈ 3.8 Pa (≈ 2.5 m/s), confirming the 9 V battery as the main limit.
- The gain levels off above PWM 200, which suggests the L298N now limits the fan.
- Two further runs on the same day were discarded because the sensor zero shifted by several pascals during them.

## Limitations

Validation could not be completed with this rig:

1. **No independent measurement:** velocity is derived from the Pitot reading with V = √(2Δp/ρ), the same relation as the analytical model, so the measured points fall on the model's curve at any speed. A second, independent measurement is needed.
2. **Velocity range:** even after the power upgrade, the flow reached only ≈ 2.5 m/s, below the models' 5 m/s minimum. The L298N drops about 2 V internally and is rated for about 2 A per channel, below the fan's rated current, and the unsealed joints add losses.
3. **Sensor:** the ±2 kPa sensor gives ≈ 4.9 Pa per ADC count, larger than the signal, and its zero drifted by several pascals in two re-runs.
4. **Calibration and coverage:** the sensor was zeroed but not calibrated against a reference pressure, and the Pitot tube was at a single position.

**Path to validation:**
- Add a wall static tap at the contraction inlet. The inlet-to-test-section pressure drop divided by the measured dynamic pressure should equal 1 − 1/C_R² ≈ 0.67, a speed-independent test that works at the speeds this rig already reaches. An anemometer is the alternative.
- Use a lower-range digital differential sensor (±125 to ±500 Pa).
- Replace the L298N with a MOSFET driver, power the fan from a 12 V supply rated above 3 A, and seal the joints.
