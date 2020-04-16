# Basic animation in Matplotlib.
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from numpy import exp, pi, sqrt, linspace

fig = plt.figure

# Make a first plot

def frame(args):
    frame_no, s, x, lines = args
    y = f(x, m, s)
    lines[0].set_data(x, y)
    return lines


def init():
    lines[0].set_data([], [])  # empty plot
    return lines


def f(x, m, s):
    return (1.0 / (sqrt(2 * pi) * s)) * exp(-0.5 * ((x - m) / s) ** 2)


m = 0
s_min = 0.2
s_max = 2
x = linspace(m - 3 * s_max, m + 3 * s_max, 1000)
s_values = linspace(s_max, s_min, 30)
y = f(x, m, s_max)

max_f = f(m, m, s_min)

lines = plt.plot(x, y)
plt.axis([x[0], x[-1], -0.1, max_f])
plt.xlabel('x')
plt.ylabel('f')
s = np.array(0.2, 2, 0.1)
frame_no = np.array(0.2, 2, 0.1)
all_args = (frame_no, s, x, lines)


anim = animation.FuncAnimation(fig, frame, all_args, interval=150, init_func=init, blit=True)

plt.plot()
plt.show()

