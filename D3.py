import matplotlib.animation as animation
from scipy.integrate import odeint
from numpy import arange
from pylab import *
from matplotlib.widgets import Slider, Button, RadioButtons

a = .105
b = .15
c = .3
p = .5
n = 5
ke = .1635
H = .5
c1 =.01
c2 =.5
h1 =.5
h2 =.5
e1 =.5
e2 =.5
H =.5
ke =.5
f1 =.5
f2 =.5
m =.5


#function f(h)
def PLH_gain(H):
    return e**(-ke * H)

#system where v is vector of x1, y, x2, z and t is time
def system (v, t):
    X1, X2, Y, Z = v

    dX1 = (-e1 * X1) - (c1 * Y * (X1)) + (PLH_gain(H) * h1*X1) + (f1 * ((X1 / (1 + X1))) * Z)
    dX2 = (-e2 * X2) - (c2 * Y * (X2)) + (PLH_gain(H) * h2 * X2) + (f2 * ((X2 / (1 + X2))) * Z)
    dY = (-a * Y) + ((b * X1) * (Y / (Y + 1)) * (1 - (Y / n))) + ((p *Y) * (1 / PLH_gain(H))) * (1 - (Y / n))
    dZ = (f1 * X1) + (f2 * X2) - (m * Z)

    return [dX1, dX2, dY, dZ]


fig, ax = plt.subplots()

t = arange(0, 30, .1)
#first parameter x1
#second paramter y
#third parameter 2
#four parameter z
init = [1, 1, 2, 3]
state = odeint(system, init, t)
plot(t, state[:, 0], 'y-')
figure()

plot(t, state[:, 1], 'r-')
figure()
plot(t, state[:, 2], 'c-')
figure()
plot(t, state[:, 3], 'g-')


#l11, = plt.plot(state[:, 0], state[:, 1], 'b-')

show()
#to run you can press the green triangle in the upper right hand corner