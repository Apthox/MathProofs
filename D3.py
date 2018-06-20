import matplotlib.animation as animation
import numpy
from scipy.integrate import odeint
from numpy import arange
from pylab import *
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


# function f(h)
def prey_gain(h):
    return e ** (-ke * h)


# System where v is vector of x1, y, x2, z and t is time
def system(v, t):
    X1, X2, Y, Z = v
    # dx1/dt yellow graph
    dX1 = (-e1 * X1) - (c1 * Y * (X1 / (1 + X1))) + (prey_gain(H) * h1 * (X1 / (1 + X1))) + (f1 * (X1 / (1 + X1)) * Z)

    # dx2/dt red graph
    dX2 = (-e2 * X2) - (c2 * Y * (X2 / (1 + X2))) + (c * prey_gain(H) * h2 * (X2 / (1 + X2))) + (f2 * (X2 / (1 + X2)) * Z)

    # dy/dt cyan graph
    dY = (-a * Y) + ((b * X1) * (Y / (Y + 1))) + (p * (1 / prey_gain(H))) * (Y / (Y + 1))

    # dz/dt green graph
    dZ = (f1 * X1) + (f2 * X2) - (m * Z)

    return [dX1, dX2, dY, dZ]


fig, ax = plt.subplots()

t = arange(0, 30, .1)
# [x1,x2, y, t]
init = [20, 5, 2, 3]
state = odeint(system, init, t)

# plots dX1/dt graph
for i in range(0, 1):
    c1 += .1 * i
    state = odeint(system, init, t)

    plot(t, state[:, 0])
    plt.ylabel('Aphids')
    plt.xlabel('Time')
    plt.title("dX1/dt")
figure()

# plots dX2/dt graph
plot(t, state[:, 1], 'r-')
plt.ylabel('Weevil')
plt.xlabel('Time')
plt.title("dX2/dt")
figure()

# plots dY/dt graph
plot(t, state[:, 2], 'c-')
plt.ylabel('Bath. SPP')
plt.xlabel('Time')
plt.title("dY/dt")
figure()

# plots dZ/dt graph
plot(t, state[:, 3], 'g-')
plt.ylabel('Alfalfa')
plt.xlabel('Time')
plt.title("dZ/dt")

show()
# to run you can press the green triangle in the upper right hand corner
