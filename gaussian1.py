from math import pi,sqrt,exp

s=2
m=0
x=0

const=1/(sqrt(2*pi)*s)
exponetial=exp((-1/2)*((x-m)/s)**2)
funct=const*exponetial

print('f(x) =',funct)