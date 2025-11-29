import numpy as np
import matplotlib.pyplot as plt
import math as math

h = 10**(-4)

def f(t):
    return np.sin(2*t) - 2*np.cos(t)

def df(t):
    return (f(t + h) - f(t - h)) / (2 * h)

def df2(t):
    return (f(t + h) - 2*f(t) + f(t - h)) / (h**2)

x_vals = np.linspace(0, 10, 100)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label="f(t) = sin(2t) - 2cos(t)")
plt.grid()
plt.tight_layout()
plt.show()

def bisekcija(a, b, tol=10**(-8), Nmax=200):
    fa = df(a)
    fb = df(b)
    for i in range(1, Nmax+1):
        c = 0.5 * (a + b)
        fc = df(c)
        if abs(fc) < tol or (b - a)*0.5 < tol:
            c = c
        elif fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    if df2(c) > 0:
        print(f"Pronasli smo minimum u tocki c = {c} gdje je f(c) = {f(c)}")
    else:
        print(f"Pronasli smo maksimum u tocki c = {c} gdje je f(c) = {f(c)}")

# Newton-Raphson
def newton(x0, tol=10**(-8), Nmax=200):
    x = x0
    for i in range(1, Nmax + 1):
        fx = f(x)
        dfx = df(x)
        xnew = x - fx/dfx
        if abs(xnew - x) < tol:
            if df2(xnew) > 0:
                print("Minimum")
            else:
                print("Maksimum")
            return xnew
bisekcija(1, 2)
bisekcija(3, 5)
bisekcija(5, 7)
newton(1.5)
newton(4)
newton(6)