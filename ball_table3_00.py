v0 = 100
n = 11
g = 9.8 #Projectile motion of ball given by v0*t-0.5*g*t**2
dt = 2 * v0 / g / (n - 1)
t = [i * dt for i in range(0, n)]
y = [v0 * t[i] - 0.5 * g * t[i] ** 2 for i in range(0, n)]
ty1 = [t,y]
print(ty1)
ty2 = [[tval,yval] for tval, yval in zip(t,y)]
print(ty2)
