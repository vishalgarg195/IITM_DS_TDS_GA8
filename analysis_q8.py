# analysis.py
# Financial Services CAC analysis (quarterly 2024)
# Author: 23ds2000079@ds.study.iitm.ac.in

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure output folder
out_dir = "visuals"
os.makedirs(out_dir, exist_ok=True)

# Quarterly CAC data (2024)
quarters = ["Q1", "Q2", "Q3", "Q4"]
cac_values = np.array([226.45, 225.59, 233.28, 230.13])

# Compute average and round to 2 decimals (required: 228.86)
average_cac = round(cac_values.mean(), 2)

industry_target = 150.0

# Print summary
print("Quarterly CAC values:", dict(zip(quarters, cac_values)))
print("Average CAC (2024):", average_cac)
print("Industry target CAC:", industry_target)
print()

# Put into DataFrame for convenience
df = pd.DataFrame({"quarter": quarters, "cac": cac_values})

# Set Seaborn style for professional look
sns.set_style("whitegrid")
sns.set_context("talk")

# Plot 1: Line chart with benchmark
plt.figure(figsize=(6,6), dpi=85)  # will save and then you can resize if needed
ax = sns.lineplot(data=df, x="quarter", y="cac", marker="o", linewidth=2.5)
ax.axhline(industry_target, color="#d62728", linestyle="--", linewidth=2, label=f"Industry Target ({industry_target})")
ax.axhline(average_cac, color="#2ca02c", linestyle=":", linewidth=2, label=f"Average CAC ({average_cac})")

ax.set_title("Customer Acquisition Cost (CAC) — 2024 Quarterly Trend", pad=14)
ax.set_ylabel("CAC (USD)")
ax.set_xlabel("Quarter")
ax.legend(loc="upper left")
plt.tight_layout()

trend_path = os.path.join(out_dir, "cac_trend.png")
plt.savefig(trend_path, dpi=85, bbox_inches="tight")
plt.close()

# Plot 2: Bar chart with colors showing gap to target
plt.figure(figsize=(6,6), dpi=85)
colors = ["#d62728" if v > industry_target else "#2ca02c" for v in cac_values]
ax2 = sns.barplot(x="quarter", y="cac", data=df, palette=colors)
for idx, v in enumerate(cac_values):
    ax2.text(idx, v + 2, f"{v:.2f}", ha='center', fontsize=12)
ax2.axhline(industry_target, color="#000000", linestyle="--", linewidth=1.5, label=f"Target {industry_target}")
ax2.set_title("Quarterly CAC with Industry Target")
ax2.set_ylabel("CAC (USD)")
ax2.set_xlabel("Quarter")
ax2.legend()
plt.tight_layout()

bar_path = os.path.join(out_dir, "cac_vs_target.png")
plt.savefig(bar_path, dpi=85, bbox_inches="tight")
plt.close()

# Save summary CSV
summary_df = pd.DataFrame({
    "quarter": quarters,
    "cac": cac_values
})
summary_df.to_csv("cac_quarterly_2024.csv", index=False)

# Final print to confirm files
print("Saved visuals to:", trend_path, "and", bar_path)
print("Saved data CSV to: cac_quarterly_2024.csv")
print("Average CAC in file and README should be:", average_cac)
