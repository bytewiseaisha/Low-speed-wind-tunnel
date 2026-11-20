# Experimental Validation of Analytical and Computational Low-Speed Flow Models

A 1D analytical model and a CFD model of low-speed internal flow, and a purpose-built wind tunnel to validate them experimentally.

**Author:** Aisha Awofeso · **Period:** May – November 2026

📄 **[Read the full report (PDF)](00.%20Report/Wind_Tunnel_Final_Report.pdf)**

---

## Overview

| Stage | Tool | What it does |
|---|---|---|
| Analytical model | MATLAB | 1D continuity + Bernoulli: dynamic pressure, Reynolds number, axial velocity and pressure profiles |
| CAD + fabrication | Fusion 360, FDM printing | Contraction, diffuser and fan mount printed in PETG; acrylic test section |
| CFD model | SimScale | Steady incompressible k-ω SST, 26-case parametric velocity sweep |
| Experiment | Arduino, MPXV7002DP, Pitot-static | PWM fan control (L298N), browser dashboard, 50 Hz CSV logging |
| Comparison | Python | Verification (CFD vs analytical) and validation (models vs experiment) |

## Key results

| Quantity | Value |
|---|---|
| Velocity range modelled (test section) | 5 – 30 m/s |
| Dynamic pressure (analytical) | 15.3 – 551.3 Pa |
| Reynolds number (D_h = 95 mm) | 3.2 × 10⁴ – 1.9 × 10⁵ |
| CFD pressure drop, inlet → test section | 40.5 – 1373.1 Pa, ΔP ∝ V^1.97 (R² = 0.99996) |
| **Verification:** CFD vs 1D analytical, matched geometry | CFD within 8.7% across the sweep (mean 3.4%); under 3% above ≈ 28 m/s test-section speed |
| Experimental signal at full fan speed | ≈ 1 Pa (≈ 1.2 m/s), rising steadily with PWM |
| **Validation** | Incomplete: measured speeds lie below the modelled range |

The CFD sits slightly above the analytical model at every speed, and the gap shrinks as speed rises. That matches the wall friction and turbulence losses the 1D model leaves out.

The experiment did not reach the modelled range. The fan (rated 12 V, ≈ 2.5 A) and the L298N driver were powered together from a single 9 V battery, which could supply only a small fraction of the fan's rated power. The driver's voltage drop and ≈ 2 A current limit reduced it further. The resulting signal, ≈ 1 Pa, was smaller than one ADC step of the sensor (≈ 4.9 Pa) and was resolved only through 64× oversampling. With no overlapping speed range, no model–experiment percentage error can be stated. The report explains the causes and the hardware changes needed to complete the validation.

## Tunnel geometry

| Parameter | Physical tunnel | CFD model |
|---|---|---|
| Test section (inner) | 95 × 95 × 310 mm | 92 × 92 × 376.7 mm |
| Contraction length | 234.2 mm | 234.2 mm |
| Diffuser length | 233.9 mm | 233.9 mm |
| Contraction ratio | 1.738 | 1.853 |

The physical test section was assembled by hand from 4 mm acrylic before any test section was drawn in CAD. The CFD test section was modelled afterwards with slightly different dimensions. To verify the CFD on identical geometry, the MATLAB model was run a second time with the CFD dimensions. The physical-geometry model remains the baseline for validation.

## Repository structure

```
Low-speed-wind-tunnel/
├── 00. Report/                      Full project report (PDF)
├── 01. analytical-model/            MATLAB 1D model (physical and CFD geometry) and results
├── 02. 3D Models/                   Fusion 360 / CAD files for the tunnel
├── 03. CFD Model/                   SimScale exports, consolidation script, STEP geometry
├── 04. Experimental Investigation/  Arduino firmware, logging dashboard, run data, images
└── 05. Three-Way Comparison/        Comparison script and plots
```

Each folder has its own README with details.

## Workflow

1. **Analytical:** run `low_speed_airflow_model.m` in `01` → `analytical_results.csv` and plots. `Wind_Tunnel_for_CFD.m` repeats the model on the CFD geometry for verification.
2. **CAD:** tunnel components are in `02`. The internal air volume was exported as `Wind Tunnel Air Block.step`.
3. **CFD:** the air block was simulated in SimScale, and `wind_tunnel_cfd_consolidation.py` merged the exports → `simscale_combined_results.csv`.
4. **Experiment:** `arduino_data_acquisition.ino` runs on the Arduino, and `web_logger.html` controls the fan and logs `wind_tunnel_test_1.csv` and `wind_tunnel_test_2.csv`.
5. **Comparison:** `wind_tunnel_3_way_comparison.py` loads the CFD and experimental data and produces the plots in `05. Three-Way Comparison/Results`.

## Tools

MATLAB · Autodesk Fusion · SimScale · Python (pandas, NumPy, Matplotlib, seaborn) · Arduino (C++) · HTML / CSS / JavaScript (Web Serial API) · Wokwi (firmware prototyping)

## Hardware

Arduino Uno · MPXV7002DP differential pressure sensor (±2 kPa) · Pitot tube and wall static tap · L298N motor driver · 12 V DC axial fan · 9 V battery (fan and driver supply) · Flashforge Adventurer 5M Pro (PETG) · 4 mm cast acrylic
