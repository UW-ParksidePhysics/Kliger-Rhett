# Fit density data

import numpy as np
import matplotlib.pyplot as plt

x = []  # values for temperature are a list
y = []  # Values for density are a list

infile = open('densityinfo62.py', 'r')  # Opens the file with info on the density of water
for line in infile:
    coords = line.split() # Recognizes there is a split in what the data means, temp and density
    if coords[0][0] != '#':
        x.append(float(coords[0]))  # Temp
        y.append(float(coords[1]))  # Density
infile.close()
infile2 = open('densityair.py', 'r')

x2 = []
y2 = []
for line in infile2:  # information from the density of air
    coords2 = line.split()
    if coords2[0][0] != '#':  # Start from first values for each indicated by the zeros for each axis on graph
        x2.append(float(coords2[0]))
        y2.append(float(coords2[1]))
infile2.close()

x, y = np.array(x), np.array(y)
print(x)
x2, y2 = np.array(x2), np.array(y2)
d1 = np.polyfit(x, y, 1) #1st degree polyfit for water
p1 = np.poly1d(d1)  # 1st degree poly1d for water
d12 = np.polyfit(x, y, 2)  # @nd degree polyfit for water
p12 = np.poly1d(d12)  # 2nd degree poly1d for water
#print(p1)
d2 = np.polyfit(x2, y2, 1)  # 1st degree polyfit of air
p2 = np.poly1d(d2)  #1st degree poly1d for air
d22 = np.polyfit(x2, y2, 2)
p22 = np.poly1d(d22)

#print(p2)
plt.plot(x, y, color='orange', linewidth=1.5,)  # Makes the curve orange with a linewidth of 1.5
plt.plot(x, p1(x), color='red')  # Plot the 1st degree polyfit as red
plt.plot(x, p12(x), color='yellow')  # Plot the 2nd degree polyfit as yellow


plt.plot(x2, y2, color='blue', linewidth=1.5)  # Plots the curve for the density of air as blue
plt.plot(x2, p2(x2), color='purple') # Plots the polyfit for the curve for air as first degree as purple
plt.plot(x2, p22(x2), color='green')  # Plots the polyfit for the air as a second degree as green

plt.xlabel('Degrees Celsius')  # Labels x axis as x
plt.ylabel('Density')  # Labels y axis as y
plt.show()  # Plots the info
# Above I was working on the polyfit and poly1d and I was struggling to get it to work, I commented it out to test my code without it

