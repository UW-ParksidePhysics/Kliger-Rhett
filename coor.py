xvalues = []
n = 10
a = 0.0
b = 10
h = (b-a)/float(n)
for i in range(0, n+1):
    xvalues.append(a+i*h)
print(xvalues)