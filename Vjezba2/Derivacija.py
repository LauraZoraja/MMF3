import numpy as np
import matplotlib.pyplot as plt

# Funkcija
def f(x):
    return np.exp(x)

# Analitičke derivacije
def df_exact(x):
    return np.exp(x)

def d2f_exact(x):
    return np.exp(x)

# Numeričke formule
def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_diff(f, x, h):
    return (f(x) - f(x - h)) / h

def central_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def three_point_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def five_point_diff(f, x, h):
    return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12 * h)

def second_derivative(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h)) / h**2

# Prva derivacija
x_vals_1st = [0.5, 1.5, 2.5]
h_vals = [1e-1, 1e-4, 1e-6]

print("Prva derivacija f(x) = e^x")
for x in x_vals_1st:
    print(f"\nx = {x}")
    for h in h_vals:
        exact = df_exact(x)
        fwd = forward_diff(f, x, h)
        bwd = backward_diff(f, x, h)
        ctr = central_diff(f, x, h)
        three = three_point_diff(f, x, h)
        five = five_point_diff(f, x, h)
        print(f"h = {h:.0e} | Točna vrijednost: {exact:.6f} | Unaprijed: {fwd:.6f} | Unazad: {bwd:.6f} | Centralna: {ctr:.6f} | 3-točke: {three:.6f} | 5-točki: {five:.6f}")

# Druga derivacija
x_vals_2nd = list(range(11))
h_vals_2nd = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]

errors = {x: [] for x in [1, 5, 10]}

print("\nDruga derivacija f(x) = e^x")
for x in x_vals_2nd:
    print(f"\nx = {x}")
    for h in h_vals_2nd:
        numeric = second_derivative(f, x, h)
        exact = d2f_exact(x)
        error = abs(numeric - exact)
        print(f"h = {h:.0e} | Točna: {exact:.6f} | Numerička: {numeric:.6f} | Greška: {error:.6f}")
        if x in errors:
            errors[x].append(error)

# Graf greške u log-log skali
plt.figure(figsize=(8, 6))
for x in errors:
    plt.plot(h_vals_2nd, errors[x], label=f"x = {x}", marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("h")
plt.ylabel("Greška")
plt.title("Greška druge derivacije u log-log skali")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()