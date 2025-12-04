import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------------------------------------------
# Customer Analytics: Customer Lifetime Value vs Acquisition Cost
# Generates a professional Seaborn scatterplot for business insights
# -------------------------------------------------------------------

# Set professional styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create realistic synthetic marketing data
np.random.seed(42)

n = 150  # sample size

# Customer Acquisition Cost (CAC): realistic distribution
cac = np.random.normal(loc=120, scale=30, size=n).clip(40, 250)

# Customer Lifetime Value (CLV): correlated with CAC but with variance
clv = cac * np.random.uniform(8, 14, size=n) + np.random.normal(0, 150, size=n)

# Build dataframe
df = pd.DataFrame({
    "Acquisition_Cost": cac,
    "Lifetime_Value": clv
})

# Create 512×512 figure (8 inches × 8 inches at 64 dpi)
plt.figure(figsize=(8, 8), dpi=64)

# Scatterplot
sns.scatterplot(
    data=df,
    x="Acquisition_Cost",
    y="Lifetime_Value",
    hue="Acquisition_Cost",
    palette="viridis",
    edgecolor="black",
    alpha=0.85
)

# Titles and labels
plt.title("Customer Lifetime Value vs Acquisition Cost", fontsize=18, pad=20)
plt.xlabel("Customer Acquisition Cost (USD)", fontsize=16)
plt.ylabel("Customer Lifetime Value (USD)", fontsize=16)

# Style polish
plt.legend(title="Acquisition Cost", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save final image exactly 512x512
plt.savefig("chart.png", dpi=64, bbox_inches="tight")

# Show (optional, does not affect saved file)
# plt.show()
