# 05. Three-Way Comparison

Compares the analytical model, the CFD and the experiment, in two steps:

- **Verification:** is the CFD solving the problem correctly? Checked against the independent analytical solution, on matched geometry.
- **Validation:** do the models match reality? Checked against the experimental measurements.

## Files

| File | Description |
|---|---|
| `wind_tunnel_3_way_comparison.py` | Main comparison: loads the CFD and experimental data and produces the four comparison plots |
| `wind_tunnel_3_way_comparison.ipynb` | Notebook version of the same script (Google Colab) |
| `verification_cfd_vs_matlab.py` | Verification on matched geometry: CFD vs the MATLAB model run on the CFD geometry |
| `telemetry_by_run.py` | Experimental telemetry with the two runs plotted separately |
| `Results/` | Output plots |

## How to run

All scripts read their inputs from the other folders. Run them from inside this folder:

```bash
pip install pandas numpy matplotlib seaborn

# Main comparison (four plots)
python wind_tunnel_3_way_comparison.py

# Verification on matched geometry
python verification_cfd_vs_matlab.py "../01. analytical-model/analytical_results_cfd_geometry.csv" "../03. CFD Model/simscale_combined_results.csv" "Results/cmp_verification_cfd_vs_matlab.png"

# Run-by-run telemetry
python telemetry_by_run.py "../04. Experimental Investigation/Experimental Results/wind_tunnel_test_1.csv" "../04. Experimental Investigation/Experimental Results/wind_tunnel_test_2.csv" "Results/exp_telemetry_by_run.png"
```

The main comparison saves its plots in the current folder. Copies are kept in `Results/`.

## Method

1. Analytical dynamic pressure q = ½ρV² at the CFD sweep velocities
2. CFD pressure drop ΔP = p₃₃ − p₇₁ from the consolidated results
3. Experimental data grouped by fan PWM (mean and standard deviation, groups of ≤ 5 samples dropped)
4. Experimental velocity from the Pitot relation V = √(2Δp/ρ), using positive readings
5. Verification: CFD ΔP compared with the MATLAB `P_inlet_rel_test` on the CFD geometry, at matching test-section speeds (V_t = 1.8535 × V_inlet)

## Outputs

| Plot | Shows |
|---|---|
| `analytical_vs_cfd_pressure.png` | q against CFD ΔP over the sweep |
| `cmp_verification_cfd_vs_matlab.png` | CFD ΔP against the MATLAB model on matched geometry, with % difference |
| `experimental_telemetry_pressure.png` | Fan PWM against measured pressure, both runs combined |
| `exp_telemetry_by_run.png` | Fan PWM against measured pressure, each run separately |
| `analytical_vs_experimental.png` | Experimental points on the analytical curve |
| `cfd_vs_experimental.png` | Experimental points on the CFD curve |

## Findings

**Verification (CFD vs analytical).** The first plot shows CFD ΔP about 150% above q. That gap exists because the two curves are different quantities: q is the dynamic pressure at one point, while ΔP is a static pressure drop from the inlet to the test-section wall. The like-for-like comparison uses the MATLAB model's inlet-to-test-section pressure drop, run on the CFD geometry:

| | Value |
|---|---|
| CFD above MATLAB, full sweep | 1.7 – 8.7% (mean 3.4%) |
| CFD above MATLAB, test-section speed above ≈ 28 m/s | under 3% |
| Same comparison using the physical geometry instead | ≈ 25% mean |

The CFD is higher at every speed, and the gap shrinks with speed. That matches the friction and turbulence losses the 1D model leaves out. The CFD set-up is verified.

**Validation (models vs experiment).** The measured velocities (≈ 0.5 – 1.4 m/s) lie entirely below the modelled range (5 – 30 m/s), and the signal (≈ 1 Pa) is below one ADC step of the sensor. No overlapping range exists for a percentage error, so validation is incomplete. The main cause was the power supply: one 9 V battery for both the fan and its driver (see `04. Experimental Investigation`).

**Data-handling notes:**
- The two runs have opposite signs (tubes swapped), so combining them cancels the trend in the combined PWM plot. Plotted separately, each run rises steadily with fan speed.
- Keeping only positive readings biases the derived velocity upward when noise is comparable to the signal.
- Agreement between the two models is verification, not validation: both share the same idealised geometry and flow assumptions.
