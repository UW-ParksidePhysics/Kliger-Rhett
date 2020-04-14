# Figure 5.5 in Chapter 5 Reading
from matplotlib.pyplot import *
from numpy import linspace, exp

#Is there a checker for errors in code with suggestions?
def f1(t):
    return t ** 2 * exp(-t ** 2)


def f2(t):
    return t ** 4 * exp(-t ** 2)


# Do I need to import exp?
figure()  # make separate figure
subplot(2, 1, 1)
t = linspace(0, 3, 51)  # 51 points from 0 to 3
y1 = f1(t)
y2 = f2(t)
plot(t, y1, 'r-', t, y2, 'bo')
xlabel('t')
ylabel('y')
axis([t[0], t[-1], min(y2) - 0.05, max(y2) + 0.5])
legend(['t^2*exp(-t^2)', 't^4*exp(-t^2)'])
title('Top figure')
subplot(2, 1, 2)
t3 = t[::4]
y3 = f2(t3)
plot(t, y1, 'b-', t3, y3, 'ys')
xlabel('t')
ylabel('y')
axis([0, 4, -0.2, 0.6])
legend(['t^2*exp(-t^2)’, ’t^4*exp(-t^2)'])
# savefig('tmp4.pdf') what does this do? #Saves the figure as the title in the single quotes
show()
