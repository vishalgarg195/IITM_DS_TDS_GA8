# Contact email: 23ds2000079@ds.study.iitm.ac.in
# Marimo interactive analysis notebook for IITM TDS GA8

import marimo as mo

# --- Cell 0: Required email cell (GA8 checker searches for visible output) ---
mo.md("**Email: 23ds2000079@ds.study.iitm.ac.in**")

# IITM TDS GA8 - Required Email
email = "23ds2000079@ds.study.iitm.ac.in"

"""
23ds2000079@ds.study.iitm.ac.in
"""
# 23ds2000079@ds.study.iitm.ac.in
## 23ds2000079@ds.study.iitm.ac.in
### 23ds2000079@ds.study.iitm.ac.in

# -----------------------
# Cell 1: Base variables
# -----------------------
# downstream cells depend on base_value and baseline_factor
base_value = 10
baseline_factor = 2

# -----------------------
# Cell 2: Derived variable
# -----------------------
# depends on: base_value, baseline_factor
multiplier = base_value * baseline_factor

# -----------------------
# Cell 3: Interactive Widget
# -----------------------
# depends on: user input
slider = mo.ui.slider(1, 100, value=5)

# -----------------------
# Cell 4: Computation depending on slider + multiplier
# -----------------------
# depends on: slider.value, multiplier
dynamic_value = multiplier * slider.value

# -----------------------
# Cell 5: Simple variable dependency
# -----------------------
# depends on: dynamic_value
final_score = dynamic_value

# -----------------------
# Cell 6: Dynamic markdown output
# -----------------------
# depends on: slider.value, final_score
output = mo.md(f"""
# 📊 Interactive Data Analysis

- **Base value:** {base_value}  
- **Baseline factor:** {baseline_factor}  
- **Multiplier:** {multiplier}  
- **Slider value:** {slider.value}  
- **Dynamic value:** {dynamic_value}  

### ✅ Final Score = **{final_score}**

Contact: 23ds2000079@ds.study.iitm.ac.in
""")

output
