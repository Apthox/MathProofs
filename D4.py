import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

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

plt.figure()

plt.show()
