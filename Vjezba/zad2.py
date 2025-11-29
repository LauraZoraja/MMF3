import numpy as np
import math as math
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return 9*x**4  - 8*x**2 - x - 6 + 10*math.cos(2*x)

def df(x):
    return 36*x**3 - 16*x - 1 - 20*math.sin(2*x)

def central_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def second_derivative(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h)) / h**2

h = 10**(-4)

x_vals = np.arange(-2.5, 2.5, 0.1)
x_l = []
y_l = []

for x in x_vals:
    x_l.append(x)
    y = f(x)
    y_l.append(y)

plt.plot(x_l, y_l, label='U(x)')
plt.xlabel('x')
plt.ylabel('U(x)')
plt.title('Graf funkcije U(x)')
plt.grid()
plt.legend()
#plt.show()


l_der = []
nt = []

for x in x_vals:
    y = central_diff(f, x, h)
    l_der.append(y)

def bisekcija(a, b, tol=10**(-8), Nmax=1000):
    fa = df(a)
    fb = df(b)
    #if fa * fb > 0:
      #  raise ValueError("preduvjeti nisu zadovoljeni: f(a) i f(b) moraju imati suprotne znakove")
    for i in range(1, Nmax+1):
        c = 0.5 * (a + b)
        fc = df(c)
        if abs(fc) < tol or (b - a)*0.5 < tol:
            c = c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    f_2 = second_derivative(f, c, h=10**(-4))
    if f_2 > 0:
        print('Ekstrem {} je lokalni minimum'.format(c))
    else:
        print('Ekstrem {} je lokalni maksimum'.format(c))


bisekcija(-1.5, 0.5)
bisekcija(-0.5, 0.5)
bisekcija(0.5, 2.0)


plt.plot(x_l, l_der, label='dU(x)')
plt.xlabel('x')
plt.ylabel('dU(x)')
plt.title('Graf funkcije dU(x)')
plt.grid()
plt.legend()
#plt.show()