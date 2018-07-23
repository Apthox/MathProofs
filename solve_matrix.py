from numpy import *

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

X1 = 80.8
X2 = 84.6
Y = 9.4
Z = 66.2

print(X1*Y*c1/(X1 + 1)**2 - X1*Z*l/(X1 + 1)**2 - X1*e**(-H*ke)*j/(X1 + 1)**2 - Y*c1/(X1 + 1) + Z*l/(X1 + 1) - d + e**(-H*ke)*j/(X1 + 1))

# J = [[ X1*Y*c1/(X1 + 1)**2 - X1*Z*l/(X1 + 1)**2 - X1*e**(-H*ke)*j/(X1 + 1)**2 - Y*c1/(X1 + 1) + Z*l/(X1 + 1) - d + e**(-H*ke)*j/(X1 + 1), 0 - X1*c1/(X1 + 1), X1*l/(X1 + 1)], [0, X2*Y*c2/(X2 + 1)**2 - X2*Z*f2/(X2 + 1)**2 - X2*c*e**(-H*ke)*h2/(X2 + 1)**2 - Y*c2/(X2 + 1) + Z*f2/(X2 + 1) + c*e**(-H*ke)*h2/(X2 + 1) - e2
#   -X2*c2/(X2 + 1), X2*f2/(X2 + 1)]
#  [Y*b*(-Y/n + 1)/(Y + 1) 0
#   -X1*Y*b*(-Y/n + 1)/(Y + 1)**2 - X1*Y*b/(n*(Y + 1)) + X1*b*(-Y/n + 1)/(Y + 1) - Y*e**(H*ke)*p/(Y + 1)**2 - a + e**(H*ke)*p/(Y + 1)
#   0]
#  [l
#   -X2*Y*c2/(X2 + 1) + X2*Z*f2/(X2 + 1) + X2*c*e**(-H*ke)*h2/(X2 + 1) - X2*e2 + X2*(X2*Y*c2/(X2 + 1)**2 - X2*Z*f2/(X2 + 1)**2 - X2*c*e**(-H*ke)*h2/(X2 + 1)**2 - Y*c2/(X2 + 1) + Z*f2/(X2 + 1) + c*e**(-H*ke)*h2/(X2 + 1) - e2)
#   -X2**2*c2/(X2 + 1) X2**2*f2/(X2 + 1) - m]]