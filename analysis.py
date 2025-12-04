# ============================================================
# IITM TDS GA8 - Marimo Interactive Notebook
# Contact email (required by checker): 23ds2000079@ds.study.iitm.ac.in
# ============================================================

import marimo as mo

# ------------------------------------------------------------
# Cell 0: Show email in Markdown (GA8 requires visible output)
# ------------------------------------------------------------
email = "23ds2000079@ds.study.iitm.ac.in"   # <-- MUST be in raw file
mo.md(f"**Email: {email}**")

# ------------------------------------------------------------
# Cell 1: Base variables (other cells depend on these)
# ------------------------------------------------------------
# depends on: base_value, baseline_factor
base_value = 10
baseline_factor = 3   # simple starting factor

# ------------------------------------------------------------
# Cell 2: Derived computation
# ------------------------------------------------------------
# depends on: base_value, baseline_factor
multiplier = base_value * baseline_factor

# ------------------------------------------------------------
# Cell 3: Interactive slider widget
# ------------------------------------------------------------
# depends on: user input
slider = mo.ui.slider(1, 100, value=5)

# ------------------------------------------------------------
# Cell 4: Further derived value using slider + multiplier
# ------------------------------------------------------------
# depends on: slider.value, multiplier
result_value = multiplier * slider.value

# ------------------------------------------------------------
# Cell 5: Final dependent variable
# ------------------------------------------------------------
# depends on: result_value
final_score = result_value

# ------------------------------------------------------------
# Cell 6: Dynamic markdown output
# ------------------------------------------------------------
# depends on: slider.value, final_score
mo.md(f"""
# 📊 Interactive Data Analysis (Marimo)

- **Email:** {email}  
- **Base Value:** {base_value}  
- **Baseline Factor:** {baseline_factor}  
- **Multiplier:** {multiplier}  
- **Slider Value:** {slider.value}  
- **Result Value:** {result_value}  

### ✅ Final Score = **{final_score}**
""")
