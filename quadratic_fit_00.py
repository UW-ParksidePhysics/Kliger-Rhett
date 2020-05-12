# Quadratic Fit
# Fit a quadratic polynomial to a two row Numpy array of x-y data using Numpy's polyfit function
# Return quadratic polynomial coefficients, ordered quadratic term first, then linear term, and constant term last.
import sys


def quadratic_fit(data):
    from numpy import polyfit

    un_data = zip(*data)
    data_2 = list(un_data)  # Takes data and interprets it here for specified commands

    quadratic_coefficients = polyfit(data_2[0], data_2[1], 2)
    return quadratic_coefficients


if __name__ == '__main__':
    print(quadratic_fit(sys.argv[1]))