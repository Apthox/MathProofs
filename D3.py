import matplotlib.animation as animation
from scipy.integrate import odeint
from numpy import arange
from pylab import *
from matplotlib.widgets import Slider, Button, RadioButtons

a = .105 #predator adult mortality rate
b = .15 #predator adult consumption rate of weevil
c = .3  #predator adult consumption aphids
p = .5  #predator adult pop gain from numphs
n = 10
n1 = 100
ke = .1635  #constant
H = .5
c1 =.3
c2 =.05
h1 =.2
h2 =.2
e1 =.5 #mortality of aphids
e2 =.5 #mortality of weevil
H =.5
f1 =.5  #adult pest consumption rate of alfalfa
f2 =.5
m =.5


#function f(h)
def Prey_gain(H):
    return e**(-ke * H)

#system where v is vector of x1, y, x2, z and t is time
def system (v, t):
    X1, X2, Y, Z = v
    #dx/dt yellow graph
    dX1 = (-e1 * X1) - (c1 * Y * (X1 / (1 + X1))) + ((Prey_gain(H) * h1 * X1) * (1 - (X1 / n1))) + (f1 * ((X1 / (1 + X1))) * Z)

    #dx2/dt red graph
    dX2 = (-e2 * X2) - (c2 * Y * (X2 / (1 + X2))) + (Prey_gain(H) * h2 * X2) + (f2 * ((X2 / (1 + X2))) * Z)

    #dy/dt cyan graph
    dY = (-a * Y) + ((b * X1) * (Y / (Y + 1)) * (1 - (Y / n))) + ((p *Y) * (1 / Prey_gain(H))) * (1 - (Y / n))

    #dz/dt green graph
    dZ = (f1 * X1) + (f2 * X2) - (m * Z)

    return [dX1, dX2, dY, dZ]


fig, ax = plt.subplots()

t = arange(0, 30, .1)
    #[x1,x2, y, t]
init = [20, 5, 2, 3]
state = odeint(system, init, t)

#plots dX1/dt graph
plot(t, state[:, 0], 'y-')
plt.ylabel('response')
plt.xlabel('time')
plt.title("dX1/dt")
figure()

#plots dX2/dt graph
plot(t, state[:, 1], 'r-')
plt.ylabel('response')
plt.xlabel('time')
plt.title("dX2/dt")
figure()

#plots dY/dt graph
plot(t, state[:, 2], 'c-')
plt.ylabel('response')
plt.xlabel('time')
plt.title("dY/dt")
figure()

#plots dZ/dt graph
plot(t, state[:, 3], 'g-')
plt.ylabel('response')
plt.xlabel('time')
plt.title("dZ/dt")


#l11, = plt.plot(state[:, 0], state[:, 1], 'b-')

show()
#to run you can press the green triangle in the upper right hand corner