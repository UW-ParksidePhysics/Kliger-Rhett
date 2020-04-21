# Fit density data

import numpy as np
import matplotlib.pyplot as plt

x = []  # values for temperature are a list
y = []  # Values for density are a list

infile = open('densityinfo62.py', 'r')  # Opens the file with info on the density of water
for line in infile:
    coords = line.split()  # Recognizes there is a split in what the data means, temp and density
    x.append(coords[0])  # Temp
    y.append(coords[1])  # Density
infile.close()
infile2 = open('densityair.py', 'r')

x2 = []
y2 = []
for line in infile2:  # information from the density of air
    coords2 = line.split()
    x2.append(coords2[0])
    y2.append(coords2[1])
infile2.close()

x, y = np.array(x), np.array(y)
x2, y2 = np.array(x2), np.array(y2)
#d1 = np.polyfit(x, y, 1)
#p1 = np.poly1d(d1)
#print(p1)
#d2 = np.polyfit(x2, y2, 1)
#p2 = np.poly1d(d2)
#print(p2)
plt.plot(x, y, color='green', linewidth=1.5)  # Makes the curve green with a linewidth of 1.5
plt.plot(x2, y2, color='blue', linewidth=1.5)  # Plots the curve for the density of air
plt.xlabel('Degrees Celsius')  # Labels x axis as x
plt.ylabel('Density')  # Labels y axis as y
plt.show()  # Plots the info
