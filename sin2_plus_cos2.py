from math import *
x=pi/4
ans=sin(x)**2+cos(x)**2
print('Sin^2(x) + Cos^2(x) = ',ans)

v0=3 #M/s
t=1 #seconds
a=2 #M/s**2
s = v0*t+((a*t**2)/20)
print('displacement =',s)

a=3.3
b=5.3
a2=a**2
b2=b**2
eq1_sum=a2+(2*a*b)+b2
eq2_sum=a2-(2*a*b)+b2
eq1_pow=(a+b)**2
eq2_pow=(a-b)**2
print('First equation:',eq1_sum,'=',eq1_pow)
print('Second equation:',eq2_pow,'=',eq2_pow)