from math import *

p=1.038
c=3.7
K=5.4*(10**-4)

constante=(47**(2/3)*c*(p**(1/3))/((K*(pi**2))*((4*pi/3)**2)
constantE=(67**(2/3)*c*(p**(1/3))/((K*(pi**2))*(((4*pi)/3)**2)

Tw=100
Ty=70
Tof=4
Tor=20

denomf=log((0.76*(Tof-Tw))/(Ty-Tw))
denomr=log((0.76*(Tor-Tw))/(Ty-Tw))

timef=constantE*denomf
timer=constantE*denomr


