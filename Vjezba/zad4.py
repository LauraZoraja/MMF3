import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Funkcija koja racuna interpolacijski polinom u tocki x
def lagrange_interpolacija(x_, y_, x):
    n = len(x_)
    P = 0.0
    for i in range(n):
        L = 1.0
        for j in range(n):
            if j != i:
                L *= (x - x_[j]) / (x_[i] - x_[j])
        P += y_[i] * L
    return P


x_ = [0, 50, 100, 150, 200, 250, 300]
y_ = [0.00, 0.20, 0.75, 1.20, 1.40, 1.48, 1.50]


t_vals = [i for i in range(0, 300)]  # od 1.0 do 4.1

# Ovo je za usporedan graf
y_lagrange = [lagrange_interpolacija(x_, y_, t) for t in t_vals]

cs = CubicSpline(x_, y_, bc_type="natural")
ys_3 = cs(t_vals)


# Full graf
plt.plot(t_vals, y_lagrange, label="B(H)", color="pink")
plt.scatter(x_, y_, color="teal", label="Tocke")
plt.plot(t_vals, ys_3, label="CubicSpline", color="purple", linestyle="--")
plt.title("Zadatak 4")
plt.xlabel("H[A/m]")
plt.ylabel("B[T]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()