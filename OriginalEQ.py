import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from matplotlib.widgets import Slider, Button, RadioButtons

a = .25  # predator adult mortality rate
range_a = [0.01, 1]

b = 0.24  # predator consumption rate
range_b = [.01, 1]

c = 0.12  # predator population gain from nymphs
range_c = [.01, 1]

d = .3  # pest mortality rate
range_e1 = [.01, 1]

g = .3  # pest mortality rate by predator
range_p = [.01, 1]

j = .512    # adult population gain from nymphs
range_h1 = [.01, 1]


k = .0001 # pest benefit from alfalfa
range_n1 = [0, .001]

ke = .1635  # constant


l = .003  # pest consumption rate of alfalfa;
range_f1 = [.01, 1]

H = .693147
range_H = [.01, 1]


m = .0001
range_m = [.01, 1]

n = 4 # carrying capacity
range_n = [1, 10]



def prey_gain(h):
    return np.e ** (-ke * h)


# System where v is vector of x1, y, z and t is time
def system(v, t):
    X1, Y, Z = v

    # dx1/dt yellow graph
    dX1 = - ((d * X1) - g * Y * (X1 / (1 + X1))) + (prey_gain(H) * j * X1 + l * (X1 * (Z / (1 + X1))))

    # dy/dt cyan graph
    dY = -(a * Y) + ((b * X1 * (Y / (1 + Y)) * (1 - Y / j))) + (c * Y)

    # dz/dt green graph
    dZ = (l * X1) - (m * Z)


    return [dX1, dY, dZ]


fig, axs = plt.subplots(2, 2, figsize=(10, 10))

t = np.arange(0, 30, .1)
init = [20, 2, 2]  # [x1, y, t]
state = odeint(system, init, t)

axs[0, 0].plot(t, state[:, 0], color='#800000')
axs[0, 0].set_title("X1")


axs[0, 1].plot(t, state[:, 1], color='#808000')
axs[0, 1].set_title("Y")

axs[1, 1].plot(t, state[:, 2], color='#00FF00')
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

ax_h1 = plt.axes([0.15, 0.5, 0.6, 0.03], facecolor=axcolor)

ax_e1 = plt.axes([0.15, 0.45, 0.6, 0.03], facecolor=axcolor)

ax_f1 = plt.axes([0.15, 0.4, 0.6, 0.03], facecolor=axcolor)


slider_a = Slider(ax_a, 'a ', range_a[0], range_a[1], valinit=a)
slider_b = Slider(ax_b, 'b', range_b[0], range_b[1], valinit=b)
slider_c = Slider(ax_c, 'c', range_c[0], range_c[1], valinit=c)
slider_n = Slider(ax_n, 'n', range_n[0], range_n[1], valinit=n)
slider_n1 = Slider(ax_n1, 'n1', range_n1[0], range_n1[1], valinit=k)
slider_H = Slider(ax_H, 'H', range_H[0], range_H[1], valinit=H)

slider_h1 = Slider(ax_h1, 'h1', range_h1[0], range_h1[1], valinit=j)

slider_e1 = Slider(ax_e1, 'e1', range_e1[0], range_e1[1], valinit=d)

slider_f1 = Slider(ax_f1, 'f1', range_f1[0], range_f1[1], valinit=l)



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
    k = slider_n1.val
    global c1

    global H
    H = slider_H.val
    global j
    j = slider_h1.val

    global d
    d = slider_e1.val

    global l
    l = slider_f1.val


    state = odeint(system, init, t)

    axs[0, 0].cla()
    axs[0, 0].plot(t, state[:, 0], color='#800000')
    axs[0, 0].set_title("X1")


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
slider_n.on_changed(update)
slider_n1.on_changed(update)

slider_H.on_changed(update)
slider_h1.on_changed(update)

slider_e1.on_changed(update)

slider_f1.on_changed(update)


plt.show()
