# Creating a Matrix in Python
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA, linspace

# We use the np.array for matrices
n = 5
d1 = np.diag(np.ones(n)*2, k=0)  # 5X5 matrix with diagonal 2s
d2 = np.diag(np.ones(n-1), k=1)  # 5X5 matrix with diagonal 1s shifted right
d3 = np.diag(np.ones(n-1), k=-1)  # 5X5 matrix with diagonal 1s shifted left
matrix = d1 + d2 +d3 #All the diagonal specified matrices added together
print(matrix) #prints all the diagonal specified matrices together
H = (1/(2*(1/(n-1)**2)))*matrix  # The desired matrix
print(H)  # Prints the desired matrix
w, v = LA.eig(H)
print(w, v)  # I believe this  prints the eigenvalues and eigenvectors of H
delta_x = 1/(n+1)
norm = np.sqrt(np.sum(np.power(v,2) * delta_x))  #normal = sqrt(sum(v**2 * delta_x))
FiveV = v[:,n-2]
print(FiveV)
x = linspace(0, 1, n+2) # Makes the plot so that it is in between 0 and 1 with 5 spaces but not including 0 or 1
plt.plot(x[1:n+1], FiveV)
plt.show()
print(norm)
