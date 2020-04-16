# Make a program that reads the first column into a list x and the second column into a list y.
# Then convert the lists to arrays,and plot the curve.Print out the maximum and minimum y coordinates.

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

infile = open('xy.dat.py', 'r')  # Open xy.dat.py and 'r' is for reading
for line in infile:
    coords = line.split()
    x.append(float(coords[0]))
    y.append(float(coords[1]))
infile.close()

x, y = np.array(x), np.array(y)

print('Minimum x value = %f' % x.min())
print('Maximum x value = %f' % x.max())
print('Minimum y value = %f' % y.min())
print('Maximum y value = %f' % y.max())

plt.plot(x, y, color='#053061', linewidth=1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.show()