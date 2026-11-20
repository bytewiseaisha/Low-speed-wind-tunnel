"""Verification: CFD pressure drop vs 1D MATLAB model run on the CFD geometry (Case B).
Usage: python verification_cfd_vs_matlab.py analytical_results_cfd_geometry.csv simscale_combined_results.csv out.png
"""
import sys, numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, seaborn as sns
sns.set_theme(style="whitegrid", palette="muted")
mat, cfd, out = sys.argv[1:4]
B = pd.read_csv(mat); B.columns = ["Vt", "q", "Re", "Vin", "dP"]
C = pd.read_csv(cfd)
CR = (B.Vt / B.Vin).mean()                     # contraction ratio implied by the MATLAB model
k = (B.dP / B.Vt**2).mean()                    # MATLAB dP = k * Vt^2 exactly (1D Bernoulli)
Vin = C["Test_Velocity_V_test_ms"].values; dp_cfd = C["Pressure_Drop_Pa"].values
Vt = CR * Vin; dp_mat = k * Vt**2; direct = Vt <= B.Vt.max()
dev = (dp_cfd - dp_mat) / dp_mat * 100

fig, (a1, a2) = plt.subplots(2, 1, figsize=(10, 8), dpi=300, sharex=True, gridspec_kw={"height_ratios": [2.2, 1]})
a1.plot(Vin, dp_cfd, "o-", color="#d62728", lw=2.2, ms=4, label="SimScale CFD ($\\Delta P = P_{33} - P_{71}$)")
a1.plot(Vin[direct], dp_mat[direct], "s", color="#1f77b4", ms=5, label="MATLAB 1D model, CFD geometry (direct output)")
a1.plot(Vin, dp_mat, "--", color="#1f77b4", lw=1.8, label="MATLAB 1D model, extended by $\\Delta P \\propto V^2$")
a1.set_ylabel("Inlet-to-test-section pressure drop (Pa)", fontsize=12, fontweight="semibold")
a1.set_title("Verification: CFD vs 1D Analytical Model on Matched Geometry", fontsize=14, fontweight="bold", pad=12)
a1.legend(fontsize=10.5, frameon=True, facecolor="white", framealpha=0.9)
a2.plot(Vin, dev, "o-", color="#2ca02c", lw=1.8, ms=4)
a2.axhline(0, color="black", lw=0.8)
a2.set_ylabel("CFD above MATLAB (%)", fontsize=12, fontweight="semibold")
a2.set_xlabel("Inlet velocity (m/s)   [test-section velocity = %.3f $\\times$ inlet]" % CR, fontsize=12, fontweight="semibold")
a2.set_ylim(0, 10)
plt.tight_layout(); plt.savefig(out)
pd.DataFrame({"Vin": Vin, "Vt": Vt, "dP_MATLAB": dp_mat, "dP_CFD": dp_cfd, "dev_pct": dev, "direct": direct}).to_csv(out.replace(".png", ".csv"), index=False)
print("CR", round(CR, 4), "dev min/mean/max", dev.min().round(2), dev.mean().round(2), dev.max().round(2))
