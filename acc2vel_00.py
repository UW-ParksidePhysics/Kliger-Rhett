# Read acceleration data and plot velocities.


import numpy as np
import matplotlib.pyplot as plt

a = 101
dt = 1

def velocity(a, dt):
    n = len(a)
    v = np.zeros(n)
    for k in np.arange(1, n):
        v[k] = v[k-1] + dt*0.5*(a[k-1] + a[k])  # Is the use of brackets accurate for what we want to do here?
    return v


acc = np.loadtxt('acc.dat_00.py')

vel = velocity(acc, dt)
time = np.array([i * dt for i in range(0, len(acc))])

plt.plot(time, acc, color='green', linewidth=1.5)
plt.plot(time, vel, color='blue', linewidth=1.5)
plt.xlabel('Time')
plt.legend(['Acceleration', 'Velocity'], loc=2)
plt.title('Time dependence of object acceleration and velocity')
plt.show()

#  Success