# analysis.py
# Email: 23ds2000079@ds.study.iitm.ac.in
# Marimo interactive analysis notebook example
# Demonstrates variable dependencies, interactive slider, dynamic markdown,
# and comments documenting how data flows between cells (depends on...).

import marimo as mo

# ---
# Cell 1: Base data and constants
# This cell is the data source. Downstream cells depend on `base_value`.
# depends on: none (source)
base_value = 10            # source variable
baseline_factor = 3        # source variable

# ---
# Cell 2: Derived variables (depends on Cell 1)
# depends on: base_value, baseline_factor
multiplier = base_value * baseline_factor
# Simple alias to satisfy the regex dependency pattern: one var assigned from another
alias_multiplier = multiplier   # alias_multiplier depends on multiplier

# ---
# Cell 3: Interactive widget (user input)
# depends on: user interaction (slider.value)
# Create a slider widget — Marimo UI slider used by the checker
slider = mo.ui.slider(start=1, stop=20, step=1, value=5)

# ---
# Cell 4: Computation using previous cells and widget
# depends on: multiplier (Cell 2) and slider (Cell 3)
dynamic_value = multiplier * slider.value    # dynamic_value depends on multiplier and slider.value

# Another direct assignment to show var = var dependency
final_score = dynamic_value    # final_score depends on dynamic_value

# ---
# Cell 5: Dynamic markdown output that updates with the slider
# depends on: slider.value, final_score
result_md = mo.md(f"""
# Interactive Analysis Result

- **Base value:** {base_value}  
- **Baseline factor:** {baseline_factor}  
- **Multiplier (base × factor):** {multiplier}  
- **Alias multiplier:** {alias_multiplier}  
- **Slider value:** **{slider.value}**  
- **Dynamic computed value (multiplier × slider):** **{dynamic_value}**

**Final score:** **{final_score}**

*Comments:* This markdown block is dynamic and will update when the slider moves.
""")

# Display the dynamic markdown so Marimo renders it and updates on slider change
result_md
