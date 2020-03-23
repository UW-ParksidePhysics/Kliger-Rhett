#Integrating a function by trapezoid rule
from scipy.lib import*
from math import*
def trapezint1(f, a, b):
    return ((b-a)/2)*(f(a)+f(b))
print(pi) #checking if these imported properly
print(cos(0))
print(sin(0))

print(trapezint1(cos, 0, pi))
print(trapezint1(sin, 0, pi))
print(trapezint1(sin, 0, pi/2))

# Part c approximating the area under the function
def trapezint2(f, a, b):
    return (b - a) / 4. * (f(a) + 2 * f((a + b) / 2.) + f(b))
print(trapezint2(cos, 0, pi))
print(trapezint2(sin, 0, pi))
print(trapezint2(sin, 0, pi/2))

f1 = (cos, 0, pi)
f2 = (sin, 0, pi)
f3 = (sin, 0, pi/2)

functions = [f1, f2, f3]
print(functions)