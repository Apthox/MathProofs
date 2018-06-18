import matplotlib.animation as animation
from scipy.integrate import odeint
from numpy import arange
from pylab import *
from matplotlib.widgets import Slider, Button, RadioButtons

def dydt_system (v, t):
    x1, y, x2, z = v
    dy = (x * y)**2
    return [t, dy]


fig, ax = plt.subplots()

t = arange(0, 30, .1)
init = [1, 1, 1, 1]
state = odeint(dydt_system, init, t)

l11, = plt.plot(state[:, 0], state[:, 1], 'b-')

show()