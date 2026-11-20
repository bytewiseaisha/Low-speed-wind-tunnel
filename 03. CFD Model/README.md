# 03. CFD Model

Steady RANS simulation of the internal tunnel flow in SimScale, run as a 26-case parametric velocity sweep.

## Files

| File | Description |
|---|---|
| `Wind Tunnel Air Block.step` | Internal air volume exported from Fusion, imported into SimScale |
| `SimScale Results/` | Raw SimScale area-average exports for each variable and face |
| `wind_tunnel_cfd_consolidation.py` | Merges the exports into one table |
| `wind_tunnel_CFD_consolidation.ipynb` | Notebook version of the same script (Google Colab) |
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

SimScale exports one CSV per variable per result control (for example `p.csv` for face 33 and `p (1).csv` for face 71). The consolidation script reads them from `SimScale Results/`, merges U_x, p, k, ω and ν_t for both faces on the run number and adds:

```
Pressure_Drop_Pa = p_face33 − p_face71
```

Run it from inside this folder:

```bash
pip install pandas
python wind_tunnel_cfd_consolidation.py
```

## Results

| Inlet U_x (m/s) | Test-section velocity (m/s) | ΔP (Pa) |
|---|---|---|
| 5 | 9.3 | 40.54 |
| 10 | 18.5 | 155.65 |
| 20 | 37.1 | 610.03 |
| 30 | 55.6 | 1373.11 |

- ΔP ∝ V^1.97 (R² = 0.99996), very close to the ideal V² law.
- **Verification:** compared with the MATLAB model run on the same CFD geometry (`01. analytical-model/Wind_Tunnel_for_CFD.m`), the CFD lies 1.7 – 8.7% above it across all 26 runs (mean 3.4%), and under 3% above ≈ 28 m/s test-section speed. The CFD is higher at every speed, which matches the friction and turbulence losses the 1D model leaves out.

## Notes for interpretation

- The column `Test_Velocity_V_test_ms` is the **inlet** velocity (face 33). Because of the contraction, the test-section velocity is 1.8535 × higher.
- ΔP is a **static pressure drop** between two stations, not a dynamic pressure. Comparing it directly with q = ½ρV² gives a gap of about 150%, which reflects the different quantities, not an error.
- Face 71 is a **wall**, so its k, ω and ν_t describe the near-wall region, not the core flow. ω on face 71 stays constant for runs 1 – 13.
- Residuals level off at about 10⁻² (p) to 10⁻⁴ (ω) instead of falling further, which suggests mild unsteadiness, likely at the diffuser exit. The absolute face pressures scatter at high speed, but ΔP stays smooth.
- The CFD test section is smaller than the physical one (see `02. 3D Models`). No mesh-independence study was carried out.
