# Fit curve array
# Make fit curve using fit polynomial coefficients, NumPy's polyval, and minimum and maximum x-values
import quadratic_fit_00 as qf
import numpy as np
import matplotlib.pyplot as plt
# polyval(p,x)
qf.quadratic_coefficients = np.linspace(-10, 10, 100)  # Has linespace from -10 to 10 with 100 points in between
print(min(qf.quadratic_coefficients))
print(max(qf.quadratic_coefficients))

p1 = np.polyval(qf.quadratic_coefficients, 'integer') # Place an integer where integer is
print(p1)