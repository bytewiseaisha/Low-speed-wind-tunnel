import sys, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, seaborn as sns
sns.set_theme(style="whitegrid", palette="muted")
f1, f2, out = sys.argv[1:4]
plt.figure(figsize=(10, 6), dpi=300)
for f, lab, col, ec in [(f1, "Run 1", "#2ca02c", "#98df8a"), (f2, "Run 2 (Pitot/static tubes swapped)", "#9467bd", "#c5b0d5")]:
    d = pd.read_csv(f)
    s = d.groupby("FanPWM")["Pressure_Pa"].agg(["count", "mean", "std"]).reset_index()
    s = s[s["count"] > 5]
    plt.errorbar(s["FanPWM"], s["mean"], yerr=s["std"], fmt="o-", color=col, ecolor=ec,
                 elinewidth=1.2, capsize=2, markersize=4, linewidth=1.2, label=lab)
plt.axhline(0, color="black", linewidth=0.8)
plt.title("Experimental Telemetry by Run: Fan PWM vs. Measured Differential Pressure", fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Fan Speed Throttle (PWM: 0 - 255)", fontsize=12, fontweight="semibold")
plt.ylabel("Measured Differential Pressure ($\\Delta P_{exp}$ [Pa])", fontsize=12, fontweight="semibold")
plt.legend(fontsize=11, frameon=True, facecolor="white", framealpha=0.9)
plt.tight_layout(); plt.savefig(out)
