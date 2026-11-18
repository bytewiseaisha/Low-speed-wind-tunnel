# Experimental Validation of Analytical and Computational Low-Speed Flow Models

A 1D analytical model and a CFD model of low-speed internal flow, and a purpose-built wind tunnel to validate them experimentally.

**Author:** Aisha Awofeso · **Period:** May – November 2026

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
| Velocity range modelled | 5 – 30 m/s |
| Dynamic pressure (analytical) | 15.3 – 551.3 Pa |
| Reynolds number (D_h = 95 mm) | 3.2 × 10⁴ – 1.9 × 10⁵ |
| CFD pressure drop, inlet → test section | 40.5 – 1373.1 Pa, ΔP ∝ V^1.97 (R² = 0.99996) |
| **Verification:** CFD vs 1D analytical (like for like) | Within 3% over 15 – 30 m/s (mean 3.4% over full sweep) |
| Experimental signal at full fan speed | ≈ 1 Pa (≈ 1.2 m/s), rising steadily with PWM |
| **Validation** | Incomplete: measured speeds lie below the modelled range |

The experimental signal was smaller than one ADC step of the sensor (≈ 4.9 Pa) and was resolved only through 64× oversampling. The fan and driver current limit and the sensor range kept the flow well below 5 m/s, so no overlapping range exists for a percentage error. The full report explains the causes and the hardware changes needed to complete the validation.

## Tunnel geometry

| Parameter | Physical tunnel | CFD model |
|---|---|---|
| Test section (inner) | 95 × 95 × 310 mm | 92 × 92 × 376.7 mm |
| Contraction length | 234.2 mm | 234.2 mm |
| Diffuser length | 233.9 mm | 233.9 mm |
| Contraction ratio | 1.738 | 1.853 |

The physical test section was assembled by hand from 4 mm acrylic before any test section was drawn in CAD. The CFD test section was modelled afterwards with slightly different dimensions. This mismatch is accounted for in the comparison.

## Repository structure

```
Low-speed-wind-tunnel/
├── 01. analytical-model/            MATLAB 1D model and results
├── 02. 3D Models/                   Fusion 360 / CAD files for the tunnel
├── 03. CFD Model/                   SimScale exports, consolidation script, STEP geometry
├── 04. Experimental Investigation/  Arduino firmware, logging dashboard, run data
└── 05. Three-Way Comparison/        Comparison script and plots
```

Each folder has its own README with details.

## Workflow

1. **Analytical:** run the MATLAB script in `01` → `analytical_results.csv` and plots.
2. **CAD:** tunnel components in `02`; the internal air volume was exported as `wind_tunnel_air_block.step`.
3. **CFD:** air block simulated in SimScale; exports merged by `consolidation.py` → `simscale_combined_results.csv`.
4. **Experiment:** firmware on the Arduino, `logger.html` used to control the fan and log `Run_01.csv` and `Run_02.csv`.
5. **Comparison:** `comparison.py` loads the CFD and experimental data and produces the plots in `05/Results`.

## Tools

MATLAB · Autodesk Fusion · SimScale · Python (pandas, NumPy, Matplotlib, seaborn) · Arduino (C++) · HTML / CSS / JavaScript (Web Serial API)

## Hardware

Arduino Uno · MPXV7002DP differential pressure sensor (±2 kPa) · Pitot tube and wall static tap · L298N motor driver · 12 V DC axial fan · Flashforge Adventurer 5M Pro (PETG) · 4 mm cast acrylic
