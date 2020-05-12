# Fit curve array
# Make fit curve using fit polynomial coefficients, NumPy's polyval, and minimum and maximum x-values
import sys


def fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=10):
    import numpy as np
    try:
        x = np.linspace(min_x, max_x, number_of_points)  # Plot goes from minimum x value to maximum x value with number of points given
    except ArithmeticError:  # The maximum x must be larger than the minimum for x.
        if max_x < min_x:
            print("Max_x less than min_x.")

    try:
        y = np.polyval(quadratic_coefficients, x)
    except IndexError:
        if number_of_points <= 2:
            print('Index Error: Your number of points is less than 2.')

    # fit_curve = np.array(list(zip(x, y)))
    fit_curve = np.vstack((x, y)).T
    return fit_curve


if __name__ == '__main__':
    print(fit_curve_array(sys.argv[1]))