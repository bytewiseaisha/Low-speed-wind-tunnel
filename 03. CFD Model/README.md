# 03. CFD Model

Steady RANS simulation of the internal tunnel flow in SimScale, run as a 26-case parametric velocity sweep.

## Files

| File | Description |
|---|---|
| `wind_tunnel_air_block.step` | Internal air volume exported from Fusion, imported into SimScale |
| `SimScale Results/` | Raw SimScale area-average exports for each variable and face |
| `consolidation.py` | Merges the exports into one table |
| `simscale_combined_results.csv` | Consolidated results, one row per run |

## Simulation set-up

| Item | Setting |
|---|---|
| Analysis | Incompressible, steady-state (SIMPLE) |
| Turbulence model | k-ω SST |
| Inlet (face 33) | Velocity inlet, parametric U_x = 5 – 30 m/s (1 m/s steps) |
| Outlet (face 3) | Pressure outlet, 0 Pa gauge |
| Walls | No-slip |
| Mesh | Standard, fineness 5, automatic boundary layers; ≈ 448,000 cells, 151,600 nodes |
| Iterations | 1000 per run |
| Result controls | Area averages on face 33 (inlet) and face 71 (test-section side wall) |

## Run strategy

1. Single test run at 10 m/s to check the set-up
2. Single runs at 5, 10, 15, 20, 25 and 30 m/s
3. Parametric sweep: 26 runs, 5 – 30 m/s

## Consolidation

SimScale exports one CSV per variable per result control (for example `p.csv` for face 33 and `p (1).csv` for face 71). `consolidation.py` reads them from `SimScale Results/`, merges U_x, p, k, ω and ν_t for both faces on the run number and adds:

```
Pressure_Drop_Pa = p_face33 − p_face71
```

Run it from inside this folder:

```bash
pip install pandas
python consolidation.py
```

## Results

| Inlet U_x (m/s) | ΔP (Pa) |
|---|---|
| 5 | 40.54 |
| 10 | 155.65 |
| 20 | 610.03 |
| 30 | 1373.11 |

- ΔP ∝ V^1.97 (R² = 0.99996), very close to the ideal V² law.
- **Verification:** compared with the 1D prediction for the same stations, ΔP = ½ρV_in²(C_R² − 1) with C_R = 1.853, the CFD is within 3% over 15 – 30 m/s (mean 3.4% over the full sweep). This verifies the CFD set-up against an independent solution.

## Notes for interpretation

- The column `Test_Velocity_V_test_ms` is the **inlet** velocity (face 33). Because of the contraction, the test-section velocity is about 1.85× higher.
- Face 71 is a **wall**, so its k, ω and ν_t describe the near-wall region, not the core flow. ω on face 71 stays constant for runs 1 – 13.
- Residuals level off at about 10⁻² (p) to 10⁻⁴ (ω) instead of falling further, which suggests mild unsteadiness, likely at the diffuser exit. The absolute face pressures scatter at high speed, but ΔP stays smooth.
- The CFD test section is smaller than the physical one (see `02. 3D Models`).
