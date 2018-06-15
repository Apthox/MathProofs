import matplotlib.animation as animation
from scipy.integrate import odeint
from numpy import arange
from pylab import *

a = 0.1
b = 2

def system(initial, t):
    x, y = initial
    d_x = x * (b - y - x)
    d_y = (y * (x / (x + 1))) - (a*y)
    return [d_x, d_y]


t = arange(0, 30, .1)
init = [1, 2]
state = odeint(system, init, t)

ylabel('x / y')
xlabel('time')
plot(t, state[:, 0], 'r-')
plot(t, state[:, 1], 'g-')

fig = figure()
plot(state[:, 0], state[:, 1], 'b-', alpha=0.2)


def animate(i):
    plot(state[0:i, 0], state[0:i, 1], 'b-')


ani = animation.FuncAnimation(fig, animate, interval=1)

show()
