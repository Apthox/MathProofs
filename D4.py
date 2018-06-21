import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from matplotlib.widgets import Slider, Button, RadioButtons

a = .105  # predator adult mortality rate
b = 0.1  # Benefit to the predator of predator adult consumption rate of weevil
c = 0.3  # Negative impact of early harvesting on the weevil population
p = .5  # predator adult population gain from nymphs
n = 10
n1 = 100
ke = .1635  # constant
H = .8
c1 = .1  # Negative impact on the aphids of predator consumption of aphids
c2 = .03  # Negative impact on the weevil of predator consumption of weevil
h1 = .2
h2 = .2
e1 = .15  # mortality of aphids
e2 = .15  # mortality of weevil
f1 = .15  # aphids pest consumption rate of alfalfa
f2 = .15  # weevil pest consumption rate of alfalfa
m = .5


def prey_gain(h):
    return np.e ** (-ke * h)


# System where v is vector of x1, y, x2, z and t is time
def system(v, t):
    X1, X2, Y, Z = v
    # dx1/dt yellow graph
    dX1 = (-e1 * X1) - (c1 * Y * (X1 / (1 + X1))) + (prey_gain(H) * h1 * (X1 / (1 + X1))) + (f1 * (X1 / (1 + X1)) * Z)

    # dx2/dt red graph
    dX2 = (-e2 * X2) - (c2 * Y * (X2 / (1 + X2))) + (c * prey_gain(H) * h2 * (X2 / (1 + X2))) + (
    f2 * (X2 / (1 + X2)) * Z)

    # dy/dt cyan graph
    dY = (-a * Y) + ((b * X1) * (Y / (Y + 1))) + (p * (1 / prey_gain(H))) * (Y / (Y + 1))

    # dz/dt green graph
    dZ = (f1 * X1) + (f2 * X2) - (m * Z)

    return [dX1, dX2, dY, dZ]


fig, axs = plt.subplots(2, 2, figsize=(10, 10))

t = np.arange(0, 30, .1)
init = [20, 5, 2, 3]  # [x1,x2, y, t]
state = odeint(system, init, t)

axs[0, 0].plot(t, state[:, 0], color='#800000')
axs[0, 0].set_title("dX1/dt")

axs[1, 0].plot(t, state[:, 1], color='#FFFF00')
axs[1, 0].set_title("dX2/dt")

axs[0, 1].plot(t, state[:, 2], color='#808000')
axs[0, 1].set_title("dY/dt")

axs[1, 1].plot(t, state[:, 3], color='#00FF00')
axs[1, 1].set_title("dZ/dt")

plt.figure(figsize=(2,8))

axcolor = 'lightgoldenrodyellow'

# LEFT - BOTTOM - LENGTH - HEIGHT
ax_a = plt.axes([0.15, 0.95, 0.6, 0.03], facecolor=axcolor)
ax_b = plt.axes([0.15, 0.9, 0.6, 0.03], facecolor=axcolor)
ax_c = plt.axes([0.15, 0.85, 0.6, 0.03], facecolor=axcolor)
ax_d = plt.axes([0.15, 0.8, 0.6, 0.03], facecolor=axcolor)
ax_e = plt.axes([0.15, 0.75, 0.6, 0.03], facecolor=axcolor)
ax_f = plt.axes([0.15, 0.7, 0.6, 0.03], facecolor=axcolor)
ax_g = plt.axes([0.15, 0.65, 0.6, 0.03], facecolor=axcolor)
ax_h = plt.axes([0.15, 0.6, 0.6, 0.03], facecolor=axcolor)
ax_i = plt.axes([0.15, 0.55, 0.6, 0.03], facecolor=axcolor)
ax_j = plt.axes([0.15, 0.5, 0.6, 0.03], facecolor=axcolor)
ax_k = plt.axes([0.15, 0.45, 0.6, 0.03], facecolor=axcolor)
ax_l = plt.axes([0.15, 0.4, 0.6, 0.03], facecolor=axcolor)
ax_m = plt.axes([0.15, 0.35, 0.6, 0.03], facecolor=axcolor)
ax_n = plt.axes([0.15, 0.3, 0.6, 0.03], facecolor=axcolor)
ax_o = plt.axes([0.15, 0.25, 0.6, 0.03], facecolor=axcolor)
ax_p = plt.axes([0.15, 0.2, 0.6, 0.03], facecolor=axcolor)

slider_a = Slider(ax_a, 'a ', 0.01, 1, valinit=a)
slider_b = Slider(ax_b, 'b', 0.01, 1, valinit=b)
slider_c = Slider(ax_c, 'c', 0.01, 1, valinit=b)
slider_d = Slider(ax_d, 'p', 0.01, 1, valinit=b)
slider_e = Slider(ax_e, 'n', 0.01, 1, valinit=b)
slider_f = Slider(ax_f, 'n1', 0.01, 1, valinit=b)
slider_g = Slider(ax_g, 'H', 0.01, 1, valinit=b)
slider_h = Slider(ax_h, 'c1', 0.01, 1, valinit=b)
slider_i = Slider(ax_i, 'c2', 0.01, 1, valinit=b)
slider_j = Slider(ax_j, 'h1', 0.01, 1, valinit=b)
slider_k = Slider(ax_k, 'h2', 0.01, 1, valinit=b)
slider_l = Slider(ax_l, 'e1', 0.01, 1, valinit=b)
slider_m = Slider(ax_m, 'e2', 0.01, 1, valinit=b)
slider_n = Slider(ax_n, 'f1', 0.01, 1, valinit=b)
slider_o = Slider(ax_o, 'f2', 0.01, 1, valinit=b)
slider_p = Slider(ax_p, 'm', 0.01, 1, valinit=b)


def update(val):
    global a
    a = slider_a.val
    global b
    b = slider_b.val
    global c
    c = slider_c.val
    global d
    d = slider_d.val
    global e
    e = slider_e.val
    global f
    f = slider_f.val
    global g
    g = slider_g.val
    global h
    h = slider_h.val
    global i
    i = slider_i.val
    global j
    j = slider_j.val
    global k
    k = slider_k.val
    global l
    l = slider_l.val
    global m
    m = slider_m.val
    global n
    n = slider_n.val
    global o
    o = slider_o.val
    global p
    p = slider_p.val

    state = odeint(system, init, t)

    axs[0, 0].cla()
    axs[0, 0].plot(t, state[:, 0], color='#800000')

    axs[1, 0].cla()
    axs[1, 0].plot(t, state[:, 1], color='#FFFF00')

    axs[0, 1].cla()
    axs[0, 1].plot(t, state[:, 2], color='#808000')

    axs[1, 1].cla()
    axs[1, 1].plot(t, state[:, 3], color='#00FF00')


    fig.canvas.draw()


slider_a.on_changed(update)
slider_b.on_changed(update)
slider_c.on_changed(update)
slider_d.on_changed(update)
slider_e.on_changed(update)
slider_f.on_changed(update)
slider_g.on_changed(update)
slider_h.on_changed(update)
slider_i.on_changed(update)
slider_j.on_changed(update)
slider_k.on_changed(update)
slider_l.on_changed(update)
slider_m.on_changed(update)
slider_n.on_changed(update)
slider_o.on_changed(update)
slider_p.on_changed(update)

plt.show()
