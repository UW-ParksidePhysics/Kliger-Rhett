from math import sqrt, exp, pi


def gauss(x, m=0, s=1):
    gaussian = 1 / (sqrt(2 * pi) * s) * exp(-0.5 * ((x - m) / s) ** 2)
    return gaussian
m = -3 #Mean
s = 2 #Standard Deviation
n = 10 #Number of elements

print("      x |  gauss(x) ")
print("--------+-----------")
for x in [m - 5*s + i*(10 * s / (n - 1)) for i in range(n)]:
    print((f" {x:6.2f} | {gauss(x, m, s):6.3e} "))