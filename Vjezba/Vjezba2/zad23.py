import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as math
from scipy.interpolate import CubicSpline


def f(x):
    return 1./(math.sqrt(1-x))

x = np.linspace(-5, 0, 10)
yl = []

for i in x:
    y = f(i)
    yl.append(y)

x_ = [-5, -4.7, -1.25, -0.01]
y_ = []

for i in x_:
    y = f(i)
    y_.append(y)

print(y_)

cs = CubicSpline(x, yl, bc_type="natural")
ys = cs(x_)


# Full graf
plt.plot(x, yl, label="Izravno iz funkcije", color="pink")
plt.plot(x_, y_, label="Spline", color="teal")
plt.scatter(x_, y_, color="black", label="Tocke")
plt.title("Usporedba interpolacije i tocne funkcije")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
