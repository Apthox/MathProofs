import matplotlib.animation as animation
from scipy.integrate import odeint
from numpy import arange
from pylab import *

def system(v, t):
    x, y = v
