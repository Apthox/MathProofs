import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from matplotlib.widgets import Slider, Button, RadioButtons

a = .105  # predator adult mortality rate
range_a = [0.01, 1]

b = 0.1  # Benefit to the predator of predator adult consumption rate of weevil
range_b = [.01, 1]

c = 0.3  # Negative impact of early harvesting on the weevil population (not being used)
range_c = [.01, 1]

p = .5  # predator adult population gain from nymphs
range_p = [.01, 1]

n = 10
range_n = [1, 10]

k = 100
range_n1 = [1, 250]

ke = .1635  # constant

H = .8
range_H = [.01, 1]

c1 = .15  # Negative impact on the aphids of predator consumption of aphids; previous values used: .1,2
range_c1 = [.01, 1]

# !
c2 = .05  # Negative impact on the weevil of predator consumption of weevil; previous values used: .03
range_c2 = [.01, 1]

j = .5    # adult population gain (aphids)  # previous values used: .2
range_h1 = [.01, 1]

h2 = .3     # adult population gain (weevil) previous values used: .2
range_h2 = [.01, 1]

d = .15  # mortality of aphids; previous values used: .15, .3
range_e1 = [.01, 1]

e2 = .15  # mortality of weevil; previous values used: .15, .3
range_e2 = [.01, 1]

l = .2  # aphids pest consumption rate of alfalfa; previous values used: .15
range_f1 = [.01, 1]

f2 = .2  # weevil pest consumption rate of alfalfa; previous values used: .15,
range_f2 = [.01, 1]

m = .5
range_m = [.01, 1]


def prey_gain(h):
    return np.e ** (-ke * h)


# System where v is vector of x1, y, x2, z and t is time
def system(v, t):
    X1, X2, Y, Z = v
    # dx1/dt yellow graph
    dX1 = (-d * X1) - (c1 * Y * (X1 / (1 + X1))) + (prey_gain(H) * j * (X1 / (1 + X1))) + (l * (X1 / (1 + X1)) * Z)

    # dx2/dt red graph
    dX2 = (-e2 * X2) - (c2 * Y * (X2 / (1 + X2))) + (c * prey_gain(H) * h2 * (X2 / (1 + X2))) + (f2 * (X2 / (1 + X2)) * Z)

    # dy/dt cyan graph
            #1          2           3               4                   5                       6               7
    dY = (-a * Y) + ((b * X1) * (Y / (Y + 1)) * (1 - (Y / n)) )+ ((p * (1 / prey_gain(H))) * (Y / (Y + 1)))

    # dz/dt green graph
    dZ = (l * X1) + (f2 * X2) - (m * Z)


    return [dX1, dX2, dY, dZ]


fig, axs = plt.subplots(2, 2, figsize=(10, 10))

t = np.arange(0, 30, .1)
init = [20, 5, 2, 3]  # [x1,x2, y, t]
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
ax_b = plt.axes([0.15, 0.9, 0.6, 0.03], facecolor=axcolor)
ax_c = plt.axes([0.15, 0.85, 0.6, 0.03], facecolor=axcolor)
ax_p = plt.axes([0.15, 0.8, 0.6, 0.03], facecolor=axcolor)
ax_n = plt.axes([0.15, 0.75, 0.6, 0.03], facecolor=axcolor)
ax_n1 = plt.axes([0.15, 0.7, 0.6, 0.03], facecolor=axcolor)
ax_H = plt.axes([0.15, 0.65, 0.6, 0.03], facecolor=axcolor)
ax_c1 = plt.axes([0.15, 0.6, 0.6, 0.03], facecolor=axcolor)
ax_c2 = plt.axes([0.15, 0.55, 0.6, 0.03], facecolor=axcolor)
ax_h1 = plt.axes([0.15, 0.5, 0.6, 0.03], facecolor=axcolor)
ax_h2 = plt.axes([0.15, 0.45, 0.6, 0.03], facecolor=axcolor)
ax_e1 = plt.axes([0.15, 0.4, 0.6, 0.03], facecolor=axcolor)
ax_e2 = plt.axes([0.15, 0.35, 0.6, 0.03], facecolor=axcolor)
ax_f1 = plt.axes([0.15, 0.3, 0.6, 0.03], facecolor=axcolor)
ax_f2 = plt.axes([0.15, 0.25, 0.6, 0.03], facecolor=axcolor)

slider_a = Slider(ax_a, 'a ', range_a[0], range_a[1], valinit=a)
slider_b = Slider(ax_b, 'b', range_b[0], range_b[1], valinit=b)
slider_c = Slider(ax_c, 'c', range_c[0], range_c[1], valinit=c)
slider_p = Slider(ax_p, 'p', range_p[0], range_p[1], valinit=p)
slider_n = Slider(ax_n, 'n', range_n[0], range_n[1], valinit=n)
slider_n1 = Slider(ax_n1, 'n1', range_n1[0], range_n1[1], valinit=k)
slider_H = Slider(ax_H, 'H', range_H[0], range_H[1], valinit=H)
slider_c1 = Slider(ax_c1, 'c1', range_c1[0], range_c1[1], valinit=c1)
slider_c2 = Slider(ax_c2, 'c2', range_c2[0], range_c2[1], valinit=c2)
slider_h1 = Slider(ax_h1, 'h1', range_h1[0], range_h1[1], valinit=j)
slider_h2 = Slider(ax_h2, 'h2', range_h2[0], range_h2[1], valinit=h2)
slider_e1 = Slider(ax_e1, 'e1', range_e1[0], range_e1[1], valinit=d)
slider_e2 = Slider(ax_e2, 'e2', range_e2[0], range_e2[1], valinit=e2)
slider_f1 = Slider(ax_f1, 'f1', range_f1[0], range_f1[1], valinit=l)
slider_f2 = Slider(ax_f2, 'f2', range_f2[0], range_f2[1], valinit=f2)


def update(val):
    global a
    a = slider_a.val
    global b
    b = slider_b.val
    global c
    c = slider_c.val
    global p
    p = slider_p.val
    global n
    n = slider_n.val
    global k
    n1 = slider_n1.val
    global c1
    c1 = slider_c1.val
    global c2
    c2 = slider_c2.val
    global H
    H = slider_H.val
    global j
    h1 = slider_h1.val
    global h2
    h2 = slider_h2.val
    global d
    e1 = slider_e1.val
    global e2
    e2 = slider_e2.val
    global l
    f1 = slider_f1.val
    global f2
    f2 = slider_f2.val

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
slider_b.on_changed(update)
slider_c.on_changed(update)
slider_p.on_changed(update)
slider_n.on_changed(update)
slider_n1.on_changed(update)
slider_c1.on_changed(update)
slider_c2.on_changed(update)
slider_H.on_changed(update)
slider_h1.on_changed(update)
slider_h2.on_changed(update)
slider_e1.on_changed(update)
slider_e2.on_changed(update)
slider_f1.on_changed(update)
slider_f2.on_changed(update)

plt.show()
