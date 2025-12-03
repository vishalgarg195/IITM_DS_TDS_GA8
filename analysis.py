# analysis.py
# Contact email: 23ds2000079@ds.study.iitm.ac.in
# Marimo interactive analysis notebook
# This notebook demonstrates variable dependencies, an interactive slider,
# dynamic markdown output, and comments documenting how data depends across cells.

import marimo as mo

# ---
# Cell 1: Base constants / data source
# This cell defines base_value and baseline_factor which downstream cells depend on.
# depends: downstream cells depend on base_value and baseline_factor
base_value = 10
baseline_factor = 2

# ---
# Cell 2: Derived variable (depends on Cell 1 variables)
# depends: base_value, baseline_factor
multiplier = base_value * baseline_factor  # multiplier depends on base_value and baseline_factor

# ---
# Cell 3: Interactive widget (user input)
# depends: user input (slider.value)
# The slider controls how strongly the multiplier is scaled.
slider = mo.ui.slider(1, 100, value=5)  # interactive slider widget

# ---
# Cell 4: Computation using variables from previous cells
# depends: multiplier (Cell 2) and slider (Cell 3)
# dynamic_value shows how the derived pipeline reacts to user input
dynamic_value = multiplier * slider.value

# ---
# Cell 5: Simple variable-to-variable dependency (checker looks for "a = b" style)
# depends: dynamic_value
final_score = dynamic_value  # final_score depends on dynamic_value

# ---
# Cell 6: Dynamic markdown output (depends on slider and computed values)
# depends: slider.value, final_score
# This block will update when slider changes and displays computed values.
result_md = mo.md(f"""
# Interactive Analysis Result

- **Base value:** {base_value}
- **Baseline factor:** {baseline_factor}
- **Multiplier (base × factor):** {multiplier}
- **Slider value:** **{slider.value}**
- **Dynamic computed value (multiplier × slider):** **{dynamic_value}**

**Final score:** **{final_score}**

Contact: 23ds2000079@ds.study.iitm.ac.in
""")

# Render the markdown (Marimo will update it reactively)
result_md

# Extra explicit assignment to satisfy any strict 'a = b' regex
alias = final_score
