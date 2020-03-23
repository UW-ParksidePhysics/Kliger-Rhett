# Solving quadratic equation
from cmath import*
def roots(a, b, c):
    u = sqrt(b*b - 4*a*c) # u is the variable I use to distinguish the area under the square root in the quadratic formula
    x1 = (-b + u) / (2*a) # Quadratic formula gives two values of x
    x2 = (-b - u) / (2*a)
    return (x1,x2)
print(roots(1, 2, 3))
print(roots(1, 1, 1))
print(roots(1, 0, 0)) #Cannot divide by zero
print(roots(-1, -2, -3))