# Experimental Investigation of Low-Speed Airflow Using a Purpose-Built Wind Tunnel

**Analytical Modelling · Experimental Aerodynamics · Arduino-Based Data Acquisition**

This project investigates low-speed airflow through analytical modelling and experimental testing using a purpose-built wind tunnel. It combines theoretical predictions, CAD-based design, physical fabrication and pressure-data acquisition to establish a foundation for experimental airflow characterisation.

**Project status:** Analytical modelling, wind tunnel design and fabrication, and initial experimental data acquisition have been completed. Controlled velocity testing, further measurement checks and quantitative validation remain future work. CFD analysis has not yet been performed.

## Table of Contents

- [Overview](#overview)
- [Objectives](#objectives)
- [System Architecture](#system-architecture)
- [Wind Tunnel Design](#wind-tunnel-design)
- [Analytical Model](#analytical-model)
- [Experimental Setup](#experimental-setup)
- [Data Acquisition](#data-acquisition)
- [Repository Structure](#repository-structure)
- [Results and Current Limitations](#results-and-current-limitations)
- [Future Work](#future-work)
- [Tools and Technologies](#tools-and-technologies)
- [Author](#author)

## Overview

Wind tunnels provide a controlled environment for investigating airflow and studying aerodynamic behaviour. Analytical models can predict important flow quantities, while experimental measurements provide insight into the behaviour of a physical system.

This project establishes a theoretical baseline for low-speed airflow and develops a physical wind tunnel equipped with a differential pressure measurement system.

The analytical component was implemented in MATLAB. The physical setup uses an Arduino Uno, an MPXV7002DP differential pressure sensor and a Pitot-based measurement arrangement to record pressure data for subsequent analysis.

The current work focuses on establishing the analytical and experimental foundations needed for future quantitative comparison.

## Objectives

- Develop a MATLAB analytical model for estimating dynamic pressure and Reynolds number over a nominal velocity range of 5–30 m/s.
- Design the wind tunnel geometry using Fusion 360.
- Fabricate and assemble the physical wind tunnel.
- Integrate a Pitot-based pressure measurement arrangement with an Arduino-based data-acquisition system.
- Record and examine experimental differential pressure measurements.
- Identify the limitations of the current setup and the improvements required for quantitative validation.

## System Architecture

The project combines three main engineering components.

| Component | Implementation | Purpose |
|---|---|---|
| Analytical modelling | MATLAB | Predict dynamic pressure and Reynolds number |
| Mechanical design | Fusion 360 | Develop the wind tunnel geometry |
| Experimental measurement | Arduino Uno, MPXV7002DP sensor and Pitot-based setup | Record differential pressure over time |

The analytical model provides theoretical reference values. The fabricated wind tunnel provides the physical test environment, while the acquisition system records experimental measurements.

## Wind Tunnel Design

The wind tunnel was designed in Fusion 360 and fabricated to provide a physical platform for low-speed airflow investigation.

The geometry includes an inlet, contraction, test section and downstream diffuser. The contraction reduces the flow area toward the test section, while the diffuser provides a downstream expansion.

### Test-section specifications

| Parameter | Value |
|---|---:|
| Width | 0.095 m |
| Height | 0.095 m |
| Length | 0.310 m |
| Cross-sectional area | 0.009025 m² |
| Hydraulic diameter | 0.095 m |

The test section has a square cross-section. Its hydraulic diameter is therefore equal to its width and height.

## Analytical Model

A MATLAB model was developed to calculate airflow quantities over a nominal velocity range of **5–30 m/s**, using increments of 1 m/s.

### Assumed air properties

| Property | Symbol | Value |
|---|---|---:|
| Air density | ρ | 1.225 kg/m³ |
| Dynamic viscosity | μ | 1.81 × 10⁻⁵ Pa·s |
| Test-section hydraulic diameter | Dₕ | 0.095 m |

### 1. Dynamic pressure

Dynamic pressure is calculated using the incompressible-flow relationship:

$$\
q = \frac{1}{2}\rho V^2
$$

where:

- `q` is dynamic pressure (Pa).
- `ρ` is air density (kg/m³).
- `V` is airflow velocity (m/s).

The model predicts:

| Velocity | Dynamic pressure |
|---:|---:|
| 5 m/s | 15.31 Pa |
| 10 m/s | 61.25 Pa |
| 20 m/s | 245.00 Pa |
| 30 m/s | 551.25 Pa |

Dynamic pressure increases with the square of velocity under the assumed constant-density conditions.

### 2. Reynolds number

The Reynolds number is calculated as:

$$\
Re = \frac{\rho V D_h}{\mu}
$$

where `Dₕ` is the hydraulic diameter of the test section.

The model predicts a Reynolds number of approximately **3.22 × 10⁴** at 5 m/s and **1.93 × 10⁵** at 30 m/s.

### 3. Pitot-based velocity estimation

For incompressible flow, the ideal relationship between differential pressure and velocity is:

$$\
V = \sqrt{\frac{2\Delta p}{\rho}}
$$

where `Δp` represents the difference between stagnation and static pressure under the appropriate pressure convention.

This relationship provides the basis for converting differential pressure measurements into an estimated airflow velocity when the pressure measurement and operating conditions are suitable.

## Experimental Setup

The physical measurement arrangement consists of:

- An Arduino Uno for data acquisition.
- An MPXV7002DP differential pressure sensor.
- A Pitot tube for pressure measurement.
- A wall pressure tap connected to the other sensor port.
- A fabricated wind tunnel driven by a fixed-speed fan.

The Pitot tube and wall tap are positioned at the same distance from the contraction.

### Pressure connection convention

The Pitot tube was connected to the sensor's upper pressure port, while the wall-tap tube was connected to the lower port.

The sign of the differential pressure depends on the orientation of the pressure connections relative to the adopted convention. Reversing the connections reverses the sign of the measured pressure difference. Consequently, the sign of a recorded value must be interpreted alongside the actual sensor-port arrangement.

## Data Acquisition

The Arduino program reads the analogue sensor output, converts it to a pressure estimate and records the result with a timestamp.

The acquisition sketch includes:

- Oversampling of 64 analogue readings for each reported measurement.
- A nominal logging interval of approximately 20 ms.
- Timestamped pressure output.
- A startup zeroing routine.
- Commands for requesting a new zero reference and examining zero drift.

The experimental runs were recorded as time-series pressure data for subsequent inspection and analysis.

A zero check establishes a reference when both sensor ports experience equal pressure. It does not, by itself, establish measurement accuracy across the full operating range.

## Repository Structure

The repository is organised around the project's source code, measurements and documentation.

```text
low-speed-wind-tunnel/
├── README.md
├── analytical-model/
│   └── MATLAB source files
├── arduino/
│   └── Arduino acquisition sketch
├── data/
│   └── Raw experimental logs
├── figures/
│   └── CAD images, photographs and plots
└── report/
    └── Final project report
```

The folder contents will reflect the files actually committed to the repository. Replace the descriptive placeholders with the actual filenames as the project files are added.

## Results and Current Limitations

The analytical model establishes theoretical predictions for dynamic pressure and Reynolds number over the selected velocity range.

The initial experimental runs demonstrate timestamped pressure acquisition using the Arduino-based measurement system. The recorded data also show why sensor connection orientation, zero reference and experimental conditions must be considered when interpreting differential pressure.

The current experiments were exploratory and did not establish a complete set of calibrated airflow velocities across the 5–30 m/s range. A systematic spatial survey of the test section has also not been completed.

Therefore, quantitative validation of the analytical model across the full operating range remains outstanding.

## Future Work

Planned extensions include:

- Improve the repeatability and documentation of the zeroing procedure.
- Compare sensor readings against a suitable known pressure reference.
- Conduct controlled tests at multiple operating conditions or independently measured velocities.
- Repeat measurements to assess repeatability.
- Process experimental data in MATLAB and compare results with analytical predictions at matching conditions.
- Measure velocity at multiple test-section positions to investigate flow uniformity.
- Develop a CFD model of the wind tunnel.
- Compare analytical, computational and experimental results where matching conditions are available.

## Tools and Technologies

| Tool or component | Application |
|---|---|
| MATLAB | Analytical calculations and data analysis |
| Fusion 360 | CAD design of the wind tunnel |
| Arduino Uno | Data acquisition |
| MPXV7002DP | Differential pressure measurement |
| Pitot-based measurement arrangement | Airflow pressure investigation |
| Git and GitHub | Source control and project documentation |

## Author

**Aisha Awofeso**  
Systems Engineering  
University of Lagos, Nigeria

This repository documents the analytical modelling, physical development and preliminary experimental investigation of a purpose-built low-speed wind tunnel.
