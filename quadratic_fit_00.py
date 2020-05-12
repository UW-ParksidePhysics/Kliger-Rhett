# Quadratic Fit
# Fit a quadratic polynomial to a two row Numpy array of x-y data using Numpy's polyfit function

import numpy as np

# If what is wanted is  x and y values given and fit those values to a plot for quadratic
# Might need to read the file in, in that case use info from before
# Here is an example array
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

quadratic_coefficients = np.polyfit(x, y, 2)  # Fit values of x  and y into quadratic polynomial (degree 2)
print("Quadratic coefficients: ", quadratic_coefficients)
