from sympy import var, solve, diff
from scipy import e, linalg as LA
import numpy as np




X1, X2, Y, Z = var("X1 X2 Y Z")
d, c1, ke, H, l, j = var('d c1 ke H l j')
e2, c2, c, h2, f2 = var('e2 c2 c h2 f2')
a, b, n, p, m = var('a b n p m')

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




f1 = (-d * X1) - (c1 * Y * (X1 / (1 + X1))) + (e ** (-ke * H) * j * (X1 / (1 + X1))) + (l * (X1 / (1 + X1)) * Z)
f2 =(-e2 * X2) - (c2 * Y * (X2 / (1 + X2))) + (c * e ** (-ke * H) * h2 * (X2 / (1 + X2))) + (f2 * (X2 / (1 + X2)) * Z)
f3 = (-a * Y) + ((b * X1) * (Y / (Y + 1)) * (1 - (Y / n))) + ((p * (1 / e ** (-ke * H))) * (Y / (Y + 1)))
f4 = (l * X1) + (f2 * X2) - (m * Z)

print("Starting to solve!")

A11= diff(f1,X1)
A12= diff(f1,X2)
A13= diff(f1,Y)
A14= diff(f1,Z)



A21= diff(f2,X1)
A22= diff(f2,X2)
A23= diff(f2,Y)
A24= diff(f2,Z)


A31= diff(f3,X1)
A32= diff(f3,X2)
A33= diff(f3,Y)
A34= diff(f3,Z)

A41= diff(f4,X1)
A42= diff(f4,X2)
A43= diff(f4,Y)
A44= diff(f4,Z)

print("Solution found!")

X1 = 80.8
X2 = 84.6
Y = 9.4
Z = 66.2

A11 = A11.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})
A12 = A12.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})
A13 = A13.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})
A14 = A14.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})

A21 = A21.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})
A22 = A22.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})
A23 = A23.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})
A24 = A24.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})

A31 = A31.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})
A32 = A32.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})
A33 = A33.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})
A34 = A34.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})

A41 = A41.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})
A42 = A42.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})
A43 = A43.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})
A44 = A44.evalf(subs={X1: 80.8, X2: 84.6, Y: 9.4, Z: 66.2})

# print(str (A11))
# print(str (A12))
# print(str (A11))
# print(str (A14))
#
# print(str (A21))
# print(str (A22))
# print(str (A23))
# print(str (A24))
#
# print(str (A31))
# print(str (A32))
# print(str (A31))
# print(str (A34))
#
# print(str (A41))
# print(str (A42))
# print(str (A43))
# print(str (A44))

# J = np.matrix('A11 A12 A13 A14; A21 A22 A23 A24, A31 A32 A33 A34, A41 A42 A43 A44')
J = np.matrix([[A11, A12, A13, A14], [A21, A22, A23, A24], [A31, A32, A33, A34],[A41, A42, A43, A44]])
print(J)

print("eigen")
print(LA.eig(J))

