import matplotlib.animation as animation
from scipy.integrate import odeint
from numpy import arange
from pylab import *
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()

a = .105
b = .15
c = .3
d = .5
f = .5
h = .5
n = 5
ke = .1635
H = 3

dstep = .1

def PLH_gain(H):
    return e**(-ke * H)


def dydt_system(v, t):
    x, y = v
    dy = (-a * y) + ((b * x) * (y / (y + 1)) * (1 - (y / n))) + ((d * y) * (1/PLH_gain(H)))
    return [t, dy]

fig1, ax1 = plt.subplots()

t = arange(0, 30, .1)
init = [1, 1]
state = odeint(dydt_system, init, t)

l11, = ax1.plot(state[:, 0], state[:, 1], 'b-')

plt.subplots_adjust(bottom=0.25)

axcolor = 'lightgoldenrodyellow'

# LEFT - BOTTOM - LENGTH - HEIGHT
ax_a = plt.axes([0.15, 0.15, 0.25, 0.03], facecolor=axcolor)
ax_b = plt.axes([0.50, 0.15, 0.25, 0.03], facecolor=axcolor)

ax_d = plt.axes([0.15, 0.1, 0.25, 0.03], facecolor=axcolor)
ax_n = plt.axes([0.50, 0.1, 0.25, 0.03], facecolor=axcolor)

slider_a = Slider(ax_a, 'a', 0.01, 1, valinit=a)
slider_b = Slider(ax_b, 'b', 0.01, 1, valinit=b)
slider_d = Slider(ax_d, 'd', 0.01, 2, valinit=d)
slider_n = Slider(ax_n, 'n', 1, 10, valinit=n)


def update(val):
    global a
    a = slider_a.val
    global b
    b = slider_b.val
    global d
    d = slider_d.val
    global n
    n = slider_n.val

    state = odeint(dydt_system, init, t)
    # ax1.cla()
    ax1.plot(state[:, 0], state[:, 1], 'r-')
    fig1.canvas.draw()

    state = odeint(dydt_system, init, t)
    # ax1.cla()
    ax1.plot(state[:, 0], state[:, 1], 'r-')
    fig1.canvas.draw()


slider_a.on_changed(update)
slider_b.on_changed(update)
slider_d.on_changed(update)
slider_n.on_changed(update)


fig2, ax2 = plt.subplots()

def dx1dt_system(v, t):
    x, y = v
    dx = (-e * x) - ((c*y) * (x/(x+1))) + (PLH_gain(H) * h * x) + (f * (x/(x+1)))
    return [t ,dx]

t = arange(0, 30, .1)
init = [1, 1]
state = odeint(dx1dt_system, init, t)

l12, = ax2.plot(state[:, 0], state[:, 1], 'b-')


show()
