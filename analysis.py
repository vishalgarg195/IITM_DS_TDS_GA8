# analysis.py
# Email: 23ds2000079@ds.study.iitm.ac.in
# Marimo interactive analysis notebook
# This notebook demonstrates variable dependencies, an interactive slider,
# dynamic markdown output, and comments documenting how data depends across cells.

import marimo as mo

# ---
# Cell 1: Base constants / data source
# This cell defines base_value and baseline_factor which downstream cells depend on.
base_value = 10               # dependency source: base_value
baseline_factor = 2           # dependency source: baseline_factor

# ---
# Cell 2: Derived variable (depends on base_value)
# This cell depends on Cell 1 variables.
# depends on: base_value, baseline_factor
multiplier = base_value * baseline_factor  # multiplier depends on base_value and baseline_factor

# ---
# Cell 3: Interactive widget (user input)
# This cell creates a slider widget whose value will influence later computations.
# depends on: user input (slider.value)
slider = mo.ui.slider(start=1, stop=100, step=1, value=5)  # interactive slider

# ---
# Cell 4: Computation using variables from previous cells
# depends on: multiplier (Cell 2) and slider (Cell 3)
# dynamic_value shows how the derived pipeline reacts to user input
dynamic_value = multiplier * slider.value   # dependent computation

# ---
# Cell 5: Another dependent cell showing variable-to-variable assignment
# This demonstrates a variable assigned from another variable (dependency pattern)
# depends on: dynamic_value
final_score = dynamic_value                  # final_score depends on dynamic_value

# ---
# Cell 6: Dynamic markdown output (depends on slider and computed values)
# Create a markdown block that updates as the slider changes.
# depends on: slider.value, final_score
result_md = mo.md(f"""
# Interactive Analysis Result

- **Base value:** {base_value}  
- **Baseline factor:** {baseline_factor}  
- **Multiplier (base × factor):** {multiplier}  
- **Slider value:** **{slider.value}**  
- **Dynamic computed value (multiplier × slider):** **{dynamic_value}**

**Final score:** **{final_score}**
""")

# Display the dynamic markdown so Marimo renders it and updates when slider moves
result_md
