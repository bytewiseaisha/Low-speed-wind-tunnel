# 05. Three-Way Comparison

Compares the analytical model, the CFD and the experiment, in two steps:

- **Verification:** is the CFD solving the problem correctly? Checked against the independent analytical solution.
- **Validation:** do the models match reality? Checked against the experimental measurements.

## Files

| File | Description |
|---|---|
| `comparison.py` | Loads the CFD and experimental data, computes errors and produces the plots |
| `Results/` | Output plots |

## How to run

The script reads its inputs directly from the other folders:

- `../03. CFD Model/simscale_combined_results.csv`
- `../04. Experimental Investigation/Run_01.csv` and `Run_02.csv`

Run it from inside this folder:

```bash
pip install pandas numpy matplotlib seaborn
python comparison.py
```

## Method

1. Analytical dynamic pressure q = ½ρV² at the CFD sweep velocities
2. CFD pressure drop ΔP = p₃₃ − p₇₁ from the consolidated results
3. Experimental data grouped by fan PWM (mean and standard deviation, groups of ≤ 5 samples dropped)
4. Experimental velocity from the Pitot relation V = √(2Δp/ρ), using positive readings

## Outputs

| Plot | Shows |
|---|---|
| `analytical_vs_cfd_pressure.png` | q against CFD ΔP over the sweep |
| `experimental_telemetry_pressure.png` | Fan PWM against measured pressure, both runs combined |
| `analytical_vs_experimental.png` | Experimental points on the analytical curve |
| `cfd_vs_experimental.png` | Experimental points on the CFD curve |

## Findings

**Verification (CFD vs analytical).** The raw plot shows CFD ΔP about 150% above q. That gap exists because the two curves are different quantities: q is the dynamic pressure at one point, while ΔP is a static pressure drop from the inlet to the test-section wall. The like-for-like 1D prediction for the same stations is ΔP = ½ρV_in²(C_R² − 1). Against it, the CFD agrees to within 3% over 15 – 30 m/s, and its ratio ΔP/q settles at 2.49 against the ideal 2.43. The CFD set-up is verified.

**Validation (models vs experiment).** The measured velocities (≈ 0.5 – 1.4 m/s) lie entirely below the modelled range (5 – 30 m/s), and the signal (≈ 1 Pa) is below one ADC step of the sensor. No overlapping range exists for a percentage error, so validation is incomplete.

**Data-handling notes:**
- The two runs have opposite signs (tubes swapped), so combining them cancels the trend in the PWM plot. Plotted separately, each run rises steadily with fan speed.
- Keeping only positive readings biases the derived velocity upward when noise is comparable to the signal.
- Agreement between the two models is not validation: both share the same idealised geometry and flow assumptions.
