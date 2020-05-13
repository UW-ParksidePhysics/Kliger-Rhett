# Read two columns
import numpy as np


def two_column_text_read(filename):
    try:
        infile = open(filename, 'r')
    except OSError:
        print('This file is not found.')
        return

    x = []
    y = []

    for line in infile:
        content = line.split()
        x.append(float(content[0]))
        y.append(float(content[1]))
    infile.close()

    data = np.vstack([x, y]).T

    return data
