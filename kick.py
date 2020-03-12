a = 0.11 #radius of football in meters
m = 0.43 #mass of football
g = 9.81 #gravitational constant
p = 1.2  #density of air
Vh = 33.3 #Velocity of hard kick in meters a second
Vs = 2.77 #Velocity of soft kick in meters a second
Cd = 0.2 #Drag coefficient
from math import pi
A = pi*a**2
print(A)
Fg = m*g
print(Fg)
Fdh = ((0.5)*Cd*p*A*(Vh**2)) #Drag force when there is a hard kick
print(Fdh)
Fds =((0.5)*Cd*p*A*(Vs**2)) #Drag force when there is a soft kick
print(Fds)