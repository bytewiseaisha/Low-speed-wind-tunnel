import sys, numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, seaborn as sns
sns.set_theme(style="whitegrid", palette="muted")
r1, r2, li, out1, out2 = sys.argv[1:6]
rho = 1.225
def summ(f, offset=0.0):
    d = pd.read_csv(f).apply(pd.to_numeric, errors="coerce").dropna()
    s = d.groupby("FanPWM")["Pressure_Pa"].agg(["count", "mean", "std"]).reset_index()
    s = s[s["count"] > 200].copy(); s["mean"] -= offset; return s
S1, S2 = summ(r1), summ(r2)
L = summ(li, offset=0.758)   # fan-off reading at the end of the Li-ion run
# Figure 1: Li-ion run with 9 V Run 1 faded for reference
plt.figure(figsize=(10, 6), dpi=300)
plt.errorbar(S1["FanPWM"], S1["mean"], yerr=S1["std"], fmt="o-", color="#2ca02c", ecolor="#98df8a",
             elinewidth=1.0, capsize=2, markersize=4, linewidth=1.2, alpha=0.35, label="Run 1: 9 V battery (for reference)")
plt.errorbar(L["FanPWM"], L["mean"], yerr=L["std"], fmt="o-", color="#d62728", ecolor="#f4a6a6",
             elinewidth=1.2, capsize=3, markersize=5, linewidth=1.8, label="Run 3: 11.1 V Li-ion (baseline-corrected)")
plt.axhline(0, color="black", lw=0.8)
plt.title("Re-run with Li-ion Supply: Fan PWM vs. Measured Differential Pressure", fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Fan Speed Throttle (PWM: 0 - 255)", fontsize=12, fontweight="semibold")
plt.ylabel("Measured Differential Pressure ($\\Delta P_{exp}$ [Pa])", fontsize=12, fontweight="semibold")
plt.legend(fontsize=11, frameon=True, facecolor="white", framealpha=0.9, loc="upper left")
plt.tight_layout(); plt.savefig(out1); plt.close()
# Figure 2: operating points vs modelled range
def bands(s):
    b = s.groupby(pd.cut(s.FanPWM, [-1, 0, 50, 100, 150, 200, 255]), observed=True)["mean"].mean()
    b = b[b > 0.05]; return np.sqrt(2 * b.values / rho), b.values
V = np.logspace(np.log10(0.3), np.log10(40), 200)
plt.figure(figsize=(10, 6), dpi=300)
plt.axvspan(5, 30, color="#1f77b4", alpha=0.08, label="Modelled range (5 – 30 m/s)")
plt.plot(V, 0.5 * rho * V**2, "--", color="#1f77b4", lw=2.2, label="Analytical $q = \\frac{1}{2}\\rho V^2$")
v1, p1 = bands(S1); vl, pl = bands(L)
plt.plot(v1, p1, "o", color="#2ca02c", ms=8, label="9 V battery (Run 1)")
plt.plot(vl, pl, "s", color="#d62728", ms=8, label="11.1 V Li-ion (Run 3)")
plt.xscale("log"); plt.yscale("log")
plt.title("Measured Operating Points vs. Modelled Range", fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Airflow Velocity ($m/s$)", fontsize=12, fontweight="semibold")
plt.ylabel("Dynamic Pressure ($Pa$)", fontsize=12, fontweight="semibold")
plt.legend(fontsize=11, frameon=True, facecolor="white", framealpha=0.9, loc="upper left")
plt.tight_layout(); plt.savefig(out2); plt.close()
print("Li-ion peak", L["mean"].max().round(2), "9V peak", S1["mean"].max().round(2))
