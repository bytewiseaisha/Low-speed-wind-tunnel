# Experimental Validation of Analytical and Computational Low-Speed Flow Models

**Analytical Modelling · Computational Fluid Dynamics · Experimental Aerodynamics**

This project investigates low-speed airflow through a purpose-built wind tunnel using analytical modelling, computational fluid dynamics (CFD) and experimental measurements.

The work combines theoretical flow modelling, wind tunnel design and fabrication, numerical simulations in SimScale, and an Arduino-based pressure measurement system. The resulting datasets are brought together for comparison, providing different perspectives on airflow behaviour within the wind tunnel.

## Project Overview

The central aim of this project is to investigate low-speed airflow in a wind tunnel test section and examine how analytical and computational predictions compare with measurements obtained from a physical setup.

The investigation is organised around three main components:

1. **Analytical Modelling:** A MATLAB model estimates airflow parameters, including dynamic pressure and Reynolds number, over a specified velocity range.
2. **Computational Fluid Dynamics:** A wind tunnel model is analysed in SimScale to obtain numerical flow data, including velocity and pressure quantities.
3. **Experimental Investigation:** A fabricated wind tunnel and an Arduino-based differential pressure measurement system are used to acquire experimental data.

The outputs from these investigations are processed and brought together through a Python-based three-way comparison.

## Project Objectives

- Develop an analytical model for estimating key low-speed airflow parameters.
- Design and fabricate a physical wind tunnel for experimental investigation.
- Develop a computational model of the wind tunnel and obtain CFD results.
- Implement a differential pressure measurement and data acquisition system.
- Acquire and process experimental measurements from the physical setup.
- Consolidate and compare analytical, computational and experimental datasets.
- Examine differences between the approaches and identify factors that may influence their agreement.

## Wind Tunnel Design

The wind tunnel was designed in Fusion 360 and fabricated to provide a physical platform for low-speed airflow investigation.

Its main sections include an inlet, contraction, test section and diffuser. The contraction reduces the flow area towards the test section, while the diffuser provides a downstream expansion.

### Test-section specifications

| Parameter | Value |
|---|---:|
| Width | 0.095 m |
| Height | 0.095 m |
| Length | 0.310 m |
| Cross-sectional area | 0.009025 m² |
| Hydraulic diameter | 0.095 m |

The test section has a square cross-section, giving a hydraulic diameter equal to its width and height.

## Analytical Modelling

The analytical model was implemented in MATLAB to estimate airflow parameters over a nominal velocity range of **5–30 m/s**, in increments of 1 m/s.

### Assumed air properties

| Property | Symbol | Value |
|---|---|---:|
| Air density | ρ | 1.225 kg/m³ |
| Dynamic viscosity | μ | 1.81 × 10⁻⁵ Pa·s |
| Test-section hydraulic diameter | Dₕ | 0.095 m |

### Dynamic pressure

Dynamic pressure is calculated using:

\[
q = \frac{1}{2}\rho V^2
\]

where:
- \(q\) is dynamic pressure (Pa).
- \(\rho\) is air density (kg/m³).
- \(V\) is airflow velocity (m/s).

### Reynolds number

The Reynolds number is calculated using:

\[
Re = \frac{\rho V D_h}{\mu}
\]

where \(D_h\) is the hydraulic diameter of the test section.

### Pitot-based velocity estimation

For incompressible flow, the ideal relationship between differential pressure and velocity is:

\[
V = \sqrt{\frac{2\Delta p}{\rho}}
\]

This relationship provides the basis for estimating airflow velocity from an appropriate differential pressure measurement.

## Computational Fluid Dynamics

The wind tunnel was modelled and simulated using **SimScale**.

The CFD investigation produced numerical results for flow quantities at selected locations within the model. Exported simulation data were processed using Python to consolidate the individual CSV files into a combined dataset.

The consolidation process brings together selected velocity, pressure and turbulence-related quantities from the simulation results.

This dataset provides the computational component of the project's three-way comparison.

## Experimental Investigation

The physical wind tunnel was equipped with a differential pressure measurement arrangement for investigating airflow behaviour.

### Experimental equipment

- Fabricated wind tunnel.
- Arduino Uno microcontroller.
- MPXV7002DP differential pressure sensor.
- Pitot tube.
- Wall pressure tap.
- Fixed-speed fan.

The Pitot tube and wall pressure tap are connected to opposite ports of the differential pressure sensor.

### Pressure connection convention

The Pitot tube is connected to the sensor's upper pressure port, while the wall pressure tap is connected to the lower port.

The sign of the measured differential pressure depends on the orientation of these connections and the adopted pressure convention. Recorded pressure values must therefore be interpreted with the sensor-port arrangement in mind.

### Data acquisition

The Arduino acquisition program reads the analogue sensor output, converts it into a pressure estimate and records timestamped measurements.

The acquisition system includes:

- Oversampling of 64 analogue readings per reported measurement.
- A nominal logging interval of approximately 20 ms.
- Timestamped pressure output.
- A startup zeroing routine.
- Commands for requesting a new zero reference and examining zero drift.

Experimental measurements were recorded in CSV format for subsequent processing and analysis.

## Three-Way Comparison

A Python-based analysis brings together the analytical, computational and experimental datasets.

The comparison is intended to examine how the three approaches represent airflow behaviour under corresponding conditions and to identify differences between their outputs.

The three datasets provide complementary perspectives:

| Approach | Data source | Role |
|---|---|---|
| Analytical | MATLAB model | Theoretical predictions |
| Computational | SimScale CFD results | Numerical flow predictions |
| Experimental | Physical wind tunnel measurements | Observed system response |

The comparison provides a basis for examining the relationship between theoretical models, numerical simulations and measurements from the fabricated wind tunnel.

## Current Scope and Limitations

The project has progressed from analytical modelling and physical fabrication to CFD simulation, experimental data acquisition and dataset comparison.

However, the existence of three datasets does not automatically establish direct equivalence between their results.

Differences in operating conditions, measurement locations, sensor calibration, modelling assumptions and simulation settings must be considered when interpreting the comparison.

The experimental runs conducted so far are exploratory. A complete calibration across the nominal 5–30 m/s velocity range and a systematic spatial survey of the test section have not been established.

Consequently, the comparison should be interpreted within the scope and limitations of the available data. Further controlled testing and measurement checks would strengthen the basis for quantitative validation.

## Repository Structure

The repository is organised into five main sections:

```text
Low-speed-wind-tunnel/
│
├── README.md
│
├── 01. analytical-model/
│
├── 02. 3D Models/
│
├── 03. CFD Model/
│
├── 04. Experimental Investigation/
│
└── 05. Three-Way Comparison/
```

Each section contains the files and resources associated with its respective stage of the investigation.

## Tools and Technologies

| Tool / Technology | Application |
|---|---|
| MATLAB | Analytical airflow modelling |
| Autodesk Fusion 360 | Wind tunnel CAD design |
| Onshape | Fan mount design |
| SimScale | Computational fluid dynamics |
| Python | Data processing, consolidation and comparison |
| Arduino IDE | Microcontroller programming |
| Arduino Uno | Experimental data acquisition |
| MPXV7002DP | Differential pressure measurement |
| 3D printing | Fabrication of selected wind tunnel components |
| Git and GitHub | Version control and project documentation |

## Author

**Aisha Awofeso**  
Systems Engineering  
University of Lagos, Nigeria

This repository documents the design, modelling, fabrication and investigation of a purpose-built low-speed wind tunnel, bringing together analytical, computational and experimental approaches to airflow characterisation.
