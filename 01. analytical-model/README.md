# 01. Analytical Model

A MATLAB model that predicts low-speed flow through the wind tunnel using 1D continuity and Bernoulli. It is the analytical baseline that the CFD is verified against and that the experiment is meant to validate.

The model is run on two geometries:

| Script | Geometry | Purpose |
|---|---|---|
| `low_speed_airflow_model.m` (and `.mlx`) | Physical test section, 95 × 95 × 310 mm | Main analytical model; baseline for experimental validation |
| `Wind_Tunnel_for_CFD.m` | CFD test section, 92 × 92 × 376.667 mm | Verification of the CFD on identical geometry |

The two scripts are identical apart from the test-section dimensions.

## Files

| File | Description |
|---|---|
| `low_speed_airflow_model.m` | Main model, physical geometry |
| `low_speed_airflow_model.mlx` | Live-script version of the main model, with outputs |
| `analytical_results.csv` | Results of the main model |
| `Wind_Tunnel_for_CFD.m` | Same model on the CFD geometry |
| `analytical_results_cfd_geometry.csv` | Results on the CFD geometry |

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

V(x) and A(x) are the local velocity and cross-sectional area at axial position x. The subscript t denotes the test section.

The contraction and diffuser walls follow a cosine profile between their end dimensions, with zero slope at each end so the walls join the test section smoothly:

```
Contraction (0 ≤ x ≤ L_c):   w(x) = w_in − (w_in − w_t) · (1 − cos(πx / L_c)) / 2
Diffuser    (0 ≤ ξ ≤ L_d):   w(x) = w_t + (w_exit − w_t) · (1 − cos(πξ / L_d)) / 2
                             where ξ = x − (L_c + L_t)
```

The height follows the same expressions, and A(x) = w(x) · h(x).

## Inputs

| Parameter | Physical geometry | CFD geometry |
|---|---|---|
| Test-section velocity | 5 – 30 m/s (1 m/s steps) | 5 – 30 m/s (1 m/s steps) |
| Test section (inner) | 95 × 95 mm, D_h = 0.095 m | 92 × 92 mm, D_h = 0.092 m |
| Test-section length | 310 mm | 376.667 mm |
| Contraction length / inlet | 234.247 mm / 125.197 × 125.305 mm | same |
| Diffuser length / exit | 233.928 mm / 125.306 × 125.306 mm | same |
| Contraction ratio | 1.738 | 1.8535 |

Section lengths were measured directly from the Fusion model. The physical test-section dimensions are those of the acrylic test section as built.

## Outputs

Each script produces:

- **Figure 1:** dynamic pressure and Reynolds number against velocity
- **Figure 2:** axial velocity and static-pressure distributions along the tunnel for every test speed
- **Results CSV:** test-section velocity, q, Re, inlet velocity and inlet static pressure relative to the test section (`P_inlet_rel_test`)

## Key results (physical geometry)

| V_t (m/s) | q (Pa) | Re | p_in − p_t (Pa) |
|---|---|---|---|
| 5 | 15.31 | 32,148 | 10.24 |
| 10 | 61.25 | 64,296 | 40.98 |
| 20 | 245.00 | 128,591 | 163.92 |
| 30 | 551.25 | 192,887 | 368.81 |

The flow is turbulent across the whole range. With no losses in the model, the static pressure lost in the contraction is fully recovered in the diffuser.

## CFD-geometry run and verification

On the CFD geometry, the inlet-to-test-section pressure drop at 30 m/s rises to 390.79 Pa, because the smaller test section gives a higher contraction ratio. Its `P_inlet_rel_test` column is the same quantity as the CFD's inlet-to-test-section pressure drop, so it is used to verify the CFD (see `05. Three-Way Comparison` and Section 7.3.2 of the report):

- The CFD lies 1.7 – 8.7% above this model across all 26 runs (mean 3.4%), and under 3% above ≈ 28 m/s test-section speed.
- The CFD is higher at every speed, and the gap shrinks with speed. Both match the friction and turbulence losses this model leaves out.
- Compared with the physical-geometry run instead, the mean difference is ≈ 25%, which shows why matching the geometry matters.

The CFD sweep velocity is applied at the **inlet**, so each CFD run corresponds to a test-section velocity of 1.8535 × V_inlet (≈ 9.3 – 55.6 m/s). This script covers test-section speeds up to 30 m/s, which matches the first 12 CFD runs directly. The remaining runs use the model's own ΔP ∝ V² relation, which is exact for the 1D model.

## How to run

Open either `.m` file in MATLAB (desktop or MATLAB Online) and run it. The figures appear, and the results CSV is written to the current folder. Run each script separately: they write to different CSV files.
