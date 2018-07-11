# dX1 = (-d * X1) - (c1 * Y * (X1 / (1 + X1))) + (prey_gain(H) * j * (X1 / (1 + X1))) + (l * (X1 / (1 + X1)) * Z)
#
# # dx2/dt red graph
# dX2 = (-e2 * X2) - (c2 * Y * (X2 / (1 + X2))) + (c * prey_gain(H) * h2 * (X2 / (1 + X2))) + (f2 * (X2 / (1 + X2)) * Z)
#
# # dy/dt cyan graph
# # 1          2           3               4                   5                       6               7
# dY = (-a * Y) + ((b * X1) * (Y / (Y + 1)) * (1 - (Y / n))) + ((p * (1 / prey_gain(H))) * (Y / (Y + 1)))
#
# # dz/dt green graph
# dZ = (l * X1) + (f2 * X2) - (m * Z)

from numpy import *
from scipy.optimize import *

# def myFunction(z):
#    x = z[0]
#    y = z[1]
#    w = z[2]
#    u = z[3]
#
#    F = empty((3))
#    F[0] = x + (2 * y) - w - 4
#    F[1] = (2*x) + y + w + 2
#    F[2] = x + (2*y) + w - 2
#    return F
#
# zGuess = array([0,0,0])
# z = fsolve(myFunction,zGuess)
# print(z)

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

def system (v):
    x1, X2, Y, Z = v

    F = empty(4)
    # X1
    F[0] = (-d * x1) - (c1 * Y * (x1 / (1 + x1))) + (e ** (-ke * H) * j * (x1 / (1 + x1))) + (l * (x1 / (1 + x1)) * Z)
    F[1] =   (-e2 * X2) - (c2 * Y * (X2 / (1 + X2))) + (c * e ** (-ke * H) * h2 * (X2 / (1 + X2))) + (f2 * (X2 / (1 + X2)) * Z)
    F[2] =   (-a * Y) + ((b * x1) * (Y / (Y + 1)) * (1 - (Y / n))) + ((p * (1 / e ** (-ke * H))) * (Y / (Y + 1)))
    F[3] = (l * x1) + (f2 * X2) - (m * Z)

    return F

zGuess = array([0,0,0,0])
z = fsolve(system,zGuess)
print(z)