# 01. Analytical Model

A MATLAB model that predicts low-speed flow through the wind tunnel using 1D continuity and Bernoulli. It is the analytical baseline that the CFD is verified against and that the experiment is meant to validate.

## Assumptions

1. Incompressible flow (constant density)
2. Constant air properties: ρ = 1.225 kg/m³, μ = 1.81 × 10⁻⁵ Pa·s
3. Steady flow
4. Temperature effects neglected
5. Uniform 1D velocity profile: no boundary layers, wall shear or losses

## Equations

| Quantity | Equation |
|---|---|
| Dynamic pressure | q = ½ρV² |
| Hydraulic diameter | D_h = 2wh / (w + h) |
| Reynolds number | Re = ρVD_h / μ |
| Continuity | V(x) = V_t · A_t / A(x) |
| Bernoulli (static pressure relative to test section) | p(x) − p_t = ½ρ(V_t² − V(x)²) |

The contraction and diffuser walls follow a cosine profile between their end dimensions:

```
w(x) = w_in − (w_in − w_t) · (1 − cos(πx / L)) / 2
```

## Inputs

| Parameter | Value |
|---|---|
| Test-section velocity | 5 – 30 m/s (1 m/s steps) |
| Test section | 95 × 95 mm, D_h = 0.095 m |
| Contraction length / inlet | 234.247 mm / 125.197 × 125.305 mm |
| Test-section length | 310 mm |
| Diffuser length / exit | 233.928 mm / 125.306 × 125.306 mm |

Section lengths were measured directly from the Fusion model. The test-section dimensions are those of the physical acrylic test section.

## Outputs

- **Figure 1:** dynamic pressure and Reynolds number against velocity
- **Figure 2:** axial velocity and static-pressure distributions along the tunnel for every test speed
- **`analytical_results.csv`:** test-section velocity, q, Re, inlet velocity and inlet static pressure relative to the test section

## Key results

| V_t (m/s) | q (Pa) | Re |
|---|---|---|
| 5 | 15.31 | 32,148 |
| 10 | 61.25 | 64,296 |
| 20 | 245.00 | 128,591 |
| 30 | 551.25 | 192,887 |

The flow is turbulent across the whole range. With no losses in the model, the static pressure lost in the contraction is fully recovered in the diffuser.

## How to run

Open the `.m` file in MATLAB (desktop or MATLAB Online) and run it. The figures appear, and `analytical_results.csv` is written to the current folder.
