# Email: 23ds2000079@ds.study.iitm.ac.in   # depends: this notebook documents dependencies

import marimo as mo

# --- Cell 1 ---
# Base variable (other cells depend on this)
x = 10

# --- Cell 2 ---
# depends on x
y = x * 2

# --- Interactive widget ---
slider = mo.ui.slider(1, 100)

# --- Dynamic Markdown output ---
mo.md(f"Slider value is: {slider.value}, and dependent variable y = {y}")
