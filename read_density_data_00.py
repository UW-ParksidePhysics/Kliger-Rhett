# plot the density versus the temperature as distinct(small) circles for each data point.

import matplotlib.pyplot as plt
import numpy as np


x = []
y = []

infile = open('densityinfo62.py', 'r')
for line in infile:
    coords = line.split()  # Lines separated by space
    if coords[0][0] != '#':  # First characters in each string, isn't number then append?
        x.append(float(coords[0]))
        y.append(float(coords[1]))
infile.close()

x, y = np.array(x), np.array(y)

plt.plot(x, y, color='green', linewidth=1.5) #makes the curve green with a linewidth of 1.5
plt.xlabel('Degrees Celsius') # Labels x axis as x
plt.ylabel('Density') # Labels y axis as y
plt.show()  #Plots the info





