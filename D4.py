import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from matplotlib.widgets import Slider, Button, RadioButtons

a = 0.25  # predator adult mortality rate
range_a = [0.001, 1]

b1 = 0.34  # Predator consumption rate of aphid
range_b1 = [.001, 1]

b2 = 0.20  # Predator consumption rate of weevil
range_b2 = [.001, 1]

c = 0.12  # Predator population gain
range_c = [.001, 1]

d1 = .3  # Aphid mortality rate
range_d1 = [.001, 1]

d2 = .6  # Weevil mortality rate
range_d2 = [.001, 1]

g1 = .3  # mortality rate of aphid by predator(wasp)
range_g1 = [.001, 1]

g2 = .4  # mortality rate of weevil by predator(wasp)
range_g2 = [.001, 1]

j1 = .5  # population gain of aphids
range_j1 = [.001, 1]

j2 = .4  # population gain of weevils
range_j2 = [.001, 1]

k1 = .01  # benefit to aphids from alfalfa
range_k1 = [.001, 1]

k2 = .03  # benefit to weevils from alfalfa
range_k2 = [.001, 1]

l1 = .003  # aphid consumption rate of alfalfa
range_l1 = [.001, 1]

l2 = .1  # weevil consumption rate of alfalfa
range_l2 = [.001, 1]

H = .89  # diversity index
range_H = [.001, 1]

m = .01  # recovery coefficient of alfalfa
range_m = [.001, 1]

n1 = 20  # carrying capacity aphid
range_n1 = [1, 30]

n2 = 10  # carrying capacity weevil
range_n2 = [1, 20]

p = .40  # ratio of weevils killed by cut
range_p = [.001, 1]

ke = .1635  # constant


def prey_gain(h):
    return np.e ** (-ke * h)


# System where v is vector of x1, y, x2, z and t is time
def system(v, t):
    X1, X2, Y, Z = v
    # dx1/dt yellow graph
    dX1 = (-d1 * X1) - ((g1 * Y) * (X1 / (1 + X1))) + (prey_gain(H) * j1 * X1) + (k1 * (X1 / (1 + X1)) * Z)

    # dx2/dt red graph
    dX2 = (-d2 * X2) - ((g2 * Y) * (X2 / (1 + X2))) + (prey_gain(H) * j2 * X2) + (k2 * (X2 / (1 + X2)) * Z) - (p * X2)

    # dy/dt cyan graph
    dY = (-a * Y) + ((b1 * X1) * (Y / (1 + Y)) * (1 - (Y / n1))) + ((b2 * X2) * (Y / (1 + Y)) * (1 - (Y / n2))) + (c * Y)

    # dz/dt green graph
    dZ = (l1 * X1) + (l2 * X2) - (m * Z)


    return [dX1, dX2, dY, dZ]


fig, axs = plt.subplots(2, 2, figsize=(10, 10))

t = np.arange(0, 14, .1)
init = [20, 20, 5, 6]  # [x1,x2, y, t]
state = odeint(system, init, t)

axs[0, 0].plot(t, state[:, 0], color='#800000')
axs[0, 0].set_title("X1")

axs[1, 0].plot(t, state[:, 1], color='#3c3293')
axs[1, 0].set_title("X2")

axs[0, 1].plot(t, state[:, 2], color='#808000')
axs[0, 1].set_title("Y")

axs[1, 1].plot(t, state[:, 3], color='#00FF00')
axs[1, 1].set_title("Z")

plt.figure(figsize=(2, 8))

axcolor = 'lightgoldenrodyellow'

# LEFT - BOTTOM - LENGTH - HEIGHT
ax_a = plt.axes([0.15, 0.95, 0.6, 0.03], facecolor=axcolor)
ax_b1 = plt.axes([0.15, 0.9, 0.6, 0.03], facecolor=axcolor)
ax_b2 = plt.axes([0.15, 0.85, 0.6, 0.03], facecolor=axcolor)
ax_c = plt.axes([0.15, 0.80, 0.6, 0.03], facecolor=axcolor)
ax_p = plt.axes([0.15, 0.75, 0.6, 0.03], facecolor=axcolor)
ax_n1 = plt.axes([0.15, 0.70, 0.6, 0.03], facecolor=axcolor)
ax_n2 = plt.axes([.15, 0.65, 0.6, 0.03], facecolor=axcolor)
ax_H = plt.axes([0.15, 0.6, 0.6, 0.03], facecolor=axcolor)
ax_d1 = plt.axes([0.15, 0.55, 0.6, 0.03], facecolor=axcolor)
ax_d2 = plt.axes([0.15, 0.5, 0.6, 0.03], facecolor=axcolor)
ax_g1 = plt.axes([0.15, 0.45, 0.6, 0.03], facecolor=axcolor)
ax_g2 = plt.axes([0.15, 0.4, 0.6, 0.03], facecolor=axcolor)
ax_j1 = plt.axes([0.15, 0.35, 0.6, 0.03], facecolor=axcolor)
ax_j2 = plt.axes([0.15, 0.3, 0.6, 0.03], facecolor=axcolor)
ax_k1 = plt.axes([0.15, 0.25, 0.6, 0.03], facecolor=axcolor)
ax_k2 = plt.axes([0.15, 0.2, 0.6, 0.03], facecolor=axcolor)
ax_l1 = plt.axes([0.15, 0.15, 0.6, 0.03], facecolor=axcolor)
ax_l2 = plt.axes([0.15, 0.10, 0.6, 0.03], facecolor=axcolor)
ax_m = plt.axes([0.15, 0.05, 0.6, 0.03], facecolor=axcolor)

slider_a = Slider(ax_a, 'a ', range_a[0], range_a[1], valinit=a)
slider_b1 = Slider(ax_b1, 'b1', range_b1[0], range_b1[1], valinit=b1)
slider_b2 = Slider(ax_b2, 'b2', range_b2[0], range_b2[1], valinit=b2)
slider_c = Slider(ax_c, 'c', range_c[0], range_c[1], valinit=c)
slider_p = Slider(ax_p, 'p', range_p[0], range_p[1], valinit=p)
slider_n1 = Slider(ax_n1, 'n1', range_n1[0], range_n1[1], valinit=n1)
slider_n2 = Slider(ax_n2, 'n2', range_n2[0], range_n2[1], valinit=n2)
slider_H = Slider(ax_H, 'H', range_H[0], range_H[1], valinit=H)
slider_d1 = Slider(ax_d1, 'd1', range_d1[0], range_d1[1], valinit=d1)
slider_d2 = Slider(ax_d2, 'd2', range_d2[0], range_d2[1], valinit=d2)
slider_g1 = Slider(ax_g1, 'g1', range_g1[0], range_g1[1], valinit=g1)
slider_g2 = Slider(ax_g2, 'g2', range_g2[0], range_g2[1], valinit=g2)
slider_j1 = Slider(ax_j1, 'j1', range_j1[0], range_j1[1], valinit=j1)
slider_j2 = Slider(ax_j2, 'j2', range_j2[0], range_j2[1], valinit=j2)
slider_k1 = Slider(ax_k1, 'k1', range_k1[0], range_k1[1], valinit=k1)
slider_k2 = Slider(ax_k2, 'k2', range_k2[0], range_k2[1], valinit=k2)
slider_l1 = Slider(ax_l1, 'l1', range_l1[0], range_l1[1], valinit=l1)
slider_l2 = Slider(ax_l2, 'l2', range_l2[0], range_l2[1], valinit=l2)
slider_m = Slider(ax_m, 'm', range_m[0], range_m[1], valinit=m)


def update(val):
    global a
    a = slider_a.val
    global b1
    b1 = slider_b1.val
    global b2
    b2 = slider_b2.val
    global c
    c = slider_c.val
    global p
    p = slider_p.val
    global n1
    n1 = slider_n1.val
    global n2
    n2 = slider_n2.val
    global d1
    d1 = slider_d1.val
    global d2
    d2 = slider_d2.val
    global g1
    g1 = slider_g1.val
    global g2
    g2 = slider_g2.val
    global H
    H = slider_H.val
    global j1
    j1 = slider_j1.val
    global j2
    j2 = slider_j2.val
    global k1
    k1 = slider_k1.val
    global k2
    k2 = slider_k2.val
    global l1
    l1 = slider_l1.val
    global l2
    l2 = slider_l2.val
    global m
    m = slider_m.val

    state = odeint(system, init, t)

    axs[0, 0].cla()
    axs[0, 0].plot(t, state[:, 0], color='#800000')
    axs[0, 0].set_title("X1")

    axs[1, 0].cla()
    axs[1, 0].plot(t, state[:, 1], color='#3c3293')
    axs[1, 0].set_title("X2")

    axs[0, 1].cla()
    axs[0, 1].plot(t, state[:, 2], color='#808000')
    axs[0, 1].set_title("Y")

    axs[1, 1].cla()
    axs[1, 1].plot(t, state[:, 3], color='#00FF00')
    axs[1, 1].set_title("Z")

    fig.canvas.draw()


slider_a.on_changed(update)
slider_b1.on_changed(update)
slider_b2.on_changed(update)
slider_c.on_changed(update)
slider_p.on_changed(update)
slider_n1.on_changed(update)
slider_n2.on_changed(update)
slider_d1.on_changed(update)
slider_d2.on_changed(update)
slider_H.on_changed(update)
slider_g1.on_changed(update)
slider_g2.on_changed(update)
slider_j1.on_changed(update)
slider_j2.on_changed(update)
slider_k1.on_changed(update)
slider_k2.on_changed(update)
slider_l1.on_changed(update)
slider_l2.on_changed(update)
slider_m.on_changed(update)

plt.show()
