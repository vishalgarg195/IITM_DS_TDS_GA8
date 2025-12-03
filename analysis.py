# Email: 23ds2000079@ds.study.iitm.ac.in
# Marimo notebook for interactive analysis

import marimo as mo

# ---
# Cell 1: Base value
# Defines a variable that later cells depend on
base_value = 10   # dependency source

# ---
# Cell 2: Interactive slider widget
# depends on: user input influences downstream calculations
slider = mo.ui.slider(start=1, stop=100, step=1, value=20)

# ---
# Cell 3: Computation using variables from previous cells
# depends on base_value and slider
scaled_value = base_value * slider.value  # another dependent variable

# ---
# Cell 4: Dynamic markdown output
# depends on scaled_value and slider
dynamic_text = mo.md(f"""
### Interactive Result

Slider value: **{slider.value}**

Computed value: **{scaled_value}**
""")

dynamic_text
