from sympy import var, solve, diff
from scipy import e, linalg as LA
import numpy as np

X1, X2, Y, Z = var("X1 X2 Y Z")
d, c1, ke, H, l, j = var('d c1 ke H l j')
e2, c2, c, h2, f2 = var('e2 c2 c h2 f2')
a, b, n, p, m, e = var('a b n p m e')

E1 = (-d * X1) - (c1 * Y * (X1 / (1 + X1))) + (e ** (-ke * H) * j * (X1 / (1 + X1))) + (l * (X1 / (1 + X1)) * Z)
E2 = (-e2 * X2) - (c2 * Y * (X2 / (1 + X2))) + (c * e ** (-ke * H) * h2 * (X2 / (1 + X2))) + (f2 * (X2 / (1 + X2)) * Z)
E3 = (-a * Y) + ((b * X1) * (Y / (Y + 1)) * (1 - (Y / n))) + ((p * (1 / e ** (-ke * H))) * (Y / (Y + 1)))
E4 = (l * X1) + (f2 * X2) - (m * Z)

A11 = diff(E1, X1)
A12 = diff(E1, X2)
A13 = diff(E1, Y)
A14 = diff(E1, Z)

A21 = diff(E2, X1)
A22 = diff(E2, X2)
A23 = diff(E2, Y)
A24 = diff(E2, Z)

A31 = diff(E3, X1)
A32 = diff(E3, X2)
A33 = diff(E3, Y)
A34 = diff(E3, Z)

A41 = diff(E4, X1)
A42 = diff(E4, X2)
A43 = diff(E4, Y)
A44 = diff(E4, Z)

print("A11: " + str(A11))
print("A12: " + str(A12))
print("A13: " + str(A13))
print("A14: " + str(A14))

print("A21: " + str(A21))
print("A22: " + str(A22))
print("A23: " + str(A23))
print("A24: " + str(A24))

print("A31: " + str(A31))
print("A32: " + str(A32))
print("A33: " + str(A33))
print("A34: " + str(A34))

print("A41: " + str(A41))
print("A42: " + str(A42))
print("A43: " + str(A43))
print("A44: " + str(A44))

a = .105
b = 0.1
c = 0.3
p = .5
n = 10
k = 100
ke = .1635
H = .8
c1 = .15
c2 = .05
j = .5
h2 = .3
d = .15
e2 = .15
l = .2
f2 = .2
m = .5

X1 = 0
X2 = 0
Y = 4.4
Z = 0
e = np.e

SA11 = eval(str(A11))
SA12 = eval(str(A12))
SA13 = eval(str(A13))
SA14 = eval(str(A14))

SA21 = eval(str(A21))
SA22 = eval(str(A22))
SA23 = eval(str(A23))
SA24 = eval(str(A24))

SA31 = eval(str(A31))
SA32 = eval(str(A32))
SA33 = eval(str(A33))
SA34 = eval(str(A34))

SA41 = eval(str(A41))
SA42 = eval(str(A42))
SA43 = eval(str(A43))
SA44 = eval(str(A44))

J1 = np.matrix([[SA11, SA12, SA13, SA14], [SA21, SA22, SA23, SA24], [SA31, SA32, SA33, SA34],[SA41, SA42, SA43, SA44]])
print(J1)

print("eigen: ")
eigen_values = LA.eig(J1)[0]
print(eigen_values)

