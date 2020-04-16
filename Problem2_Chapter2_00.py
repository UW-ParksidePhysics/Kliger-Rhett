# Problem 2 Chapter 2 The Gaussian Function
from numpy import *
import matplotlib.pyplot as plt


mu = 5  # Mean is denoted by mu and is 5 for all graphs
x = linspace(0, 10, 11)  # x is labeled between 0 and 10 in increments of 1, 11 elements
s1 = 0.5  # Standard deviation s1
s2 = 1.0  # Standard deviation s2
s3 = 1.5  # Standard deviation s3
f1 = (1 / 2 * sqrt(2 * pi * s1 ** 2)) * exp(-(x - mu) ** 2 / 2 * s1 ** 2)  # Gaussian function with sigma 0.5
f2 = (1 / 2 * sqrt(2 * pi * s2 ** 2)) * exp(-(x - mu) ** 2 / 2 * s2 ** 2)  # Gaussian function with sigma 1.0
f3 = (1 / 2 * sqrt(2 * pi * s3 ** 2)) * exp(-(x - mu) ** 2 / 2 * s3 ** 2)  # Gaussian function with sigma 1.5
plt.plot(x, f1, x, f2, x, f3)
plt.show()

