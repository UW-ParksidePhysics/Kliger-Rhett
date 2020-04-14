# Problem 4 Chapter 2 10X10 matrices
import numpy as np
from numpy import linalg as LA, linspace
import matplotlib.pyplot as plt

# We use the np.array for matrices
n = 10
d1 = np.diag(np.ones(n)*2, k=0)  # 5X5 matrix with diagonal 2s
d2 = np.diag(np.ones(n-1), k=1)  # 5X5 matrix with diagonal 1s shifted right
d3 = np.diag(np.ones(n-1), k=-1)  # 5X5 matrix with diagonal 1s shifted left
matrix = d1 + d2 + d3
print(matrix)  # Prints the matrix made up of the diagonals
H = (1/(2*(1/(n-1)**2)))*matrix  # The desired matrix
print(H)  # Prints the desired matrix
w, v = LA.eig(H)
print(w, v)  # I believe this  prints the eigenvalues and eigenvectors of H
delta_x = 1/(n+1)
norm = np.sqrt(np.sum(np.power(v,2) * delta_x)) # norm function, np.sum is sum and np.power replace the need for **(power)
TenV = v[:, n-2]/norm # I did 10-2 because the 10 is too many points to plot for the graph
print(TenV)
x = linspace(0, 1, n + 2) # Makes the plot so that it is in between 0 and 1 with 10 spaces but not including 0 or 1
plt.plot(x[1:n+1], TenV)
plt.show()
print(norm)