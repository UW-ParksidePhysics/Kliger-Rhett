# Planet orbit animation
# x = acos(wt) y = bsin(wt) # t is time, a is semi major axis of ellipse, b is semi minor axis on ellipse, w is omega and is angular velocity
# One complete orbit corresponds tot⇤[0,2pi/w]
# Each frame in the movie should be a different instance in time at x and y points.
# Velocity vector is (dxdt,dydt)=(-wasin(wt),-wbcos(wt))
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
a = 20
b = 20
w = 20
t = 60
n = 50
def data_gen():
    tlist = np.linspace(0, 2 * np.pi / w, n)  # From 0 to 2pi/w in n intervals
    for t in tlist:
        x, y = orbit_path(t, a, b, w)
        yield x, y


def init():
    ax.set_ylim(-30, 30)
    ax.set_xlim(-30, 30)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,


def orbit_path(t, a, b, w):
    return a * np.cos(w * t), b * np.sin(w * t)  # Orbit Path


#def inst_velocity(t, a, b, w):  # Instantaneous velocity magnitude
    #return w * np.sqrt((a * np.sin(w * t)) ** 2 + (b * np.cos(w * t)) ** 2)


fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.grid()
xdata, ydata = [], []


def animate_orbit(data):
    x, y = data
    #xdata.append(x)
    #ydata.append(y)
    xmin, xmax = ax.get_xlim()
    ax.scatter(x, y, c='blue')


    if x >= xmax:
        ax.set_xlim(xmin, 2 * xmax)
        ax.figure.canvas.draw()
        ax.scatter(x, y)
    #line.set_data(xdata, ydata)

    #return line,



 # Animate orbit when a=20,b=20,w=40, and n=200
ani = animation.FuncAnimation(fig, animate_orbit, data_gen, blit=False, interval=10, repeat=False, init_func=init)
plt.show()
