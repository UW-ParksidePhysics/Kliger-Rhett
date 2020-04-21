# Make a program that reads the first column into a list x and the second column into a list y.
# Then convert the lists to arrays,and plot the curve.Print out the maximum and minimum y coordinates.
# 6.1 I just assumed that would be acceptable for pycharm
import matplotlib.pyplot as plt
import numpy as np

x = []  # x is list
y = []  # y is list

infile = open('xy.dat', 'r')  # open xy.dat and 'r' is for reading # read data in xy.dat # infile looks at contents within a file
for line in infile:
    coords = line.split()
    x.append(float(coords[0]))  # appends the coordinates that are for the x part
    y.append(float(coords[1]))  # appends the coordinates that are for the y part
infile.close()  # Ends the reading of the infile

x, y = np.array(x), np.array(y)  # x and y are the arrays of info that are in the xy.dat file

print('Minimum x value = %f' % x.min())
print('Maximum x value = %f' % x.max())
print('Minimum y value = %f' % y.min())
print('Maximum y value = %f' % y.max())

plt.plot(x, y, color='green', linewidth=1.5) #makes the curve green with a linewidth of 1.5
plt.xlabel('x') # Labels x axis as x
plt.ylabel('y') # Labels y axis as y
plt.show()  #Plots the info

