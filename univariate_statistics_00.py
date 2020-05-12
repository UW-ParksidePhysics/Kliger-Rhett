# Calculate statistical characteristics of a data set

# From two_column_text_read_00.py
import sys


def univariate_statistics(data):
    from numpy import std
    un_data = zip(*data)
    data = list(un_data)
    try:
        min_x_value = min(data[0])  # Minimum x-value
        max_x_value = max(data[0])  # Maximum x-value
    except IndexError:
        if not len(data) == 2:
            print("You only need two columns of data!")
    try:
        minimum_y_value = min(data[1])  # Minimum y-value
        maximum_y_value = max(data[1])  # Maximum y-value
    except IndexError:
        if len(data[0]) or len(data[1]) <=1:
            print("You need more data points")

    # Mean
    summation = sum(data[0]) + sum(data[1])
    total = len(data[0]) + len(data[1])
    mean = summation / total

    # Standard deviation
    standard_deviation = std(data)

    # Statistics
    statistics = [mean, standard_deviation,min_x_value, max_x_value, minimum_y_value, maximum_y_value]
    return statistics


if __name__ == '__main__':
    print(univariate_statistics(sys.argv[1]))

