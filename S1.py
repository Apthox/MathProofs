import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import arange
from pylab import *


def system(v, t):
    x, y = v
    dydx = 6 * (y**2) * x
    return dy

t = arange(0, 10, .1)
state = odeint(system, 1, t)
plt.plot(t, state[:, 0])

plt.plot(t, hard_intergrated(t))

plt.show()