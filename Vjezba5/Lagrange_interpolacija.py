import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import polint as polint

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

# Funkcija koja vraca sve clanove interpolacijske sume za danu tocku x (za onaj drugi graf)
def lagrange_clanovi(x_, y_, x):
    n = len(x_)
    clanovi = []
    for i in range(n):
        L = 1.0
        for j in range(n):
            if j != i:
                L *= (x - x_[j]) / (x_[i] - x_[j])
        clanovi.append(y_[i] * L)
    return clanovi


# Tocna funkcija
def x_tocno(t):
    return -2*t - 4*t**2 + t**3

x_ = [1, 2, 3]
y_ = [-5, -12, -15]

x_2 = [1, 2, 3, 4]
y_2 = [-5, -12, -15, -8]

t_vals = [i * 0.1 for i in range(10, 41)]  # od 1.0 do 4.1

# Ovo je za usporedan graf
y_lagrange = [lagrange_interpolacija(x_, y_, t) for t in t_vals]
y_lagrange_2 = [lagrange_interpolacija(x_2, y_2, t) for t in t_vals]
y_exact = [x_tocno(t) for t in t_vals]

# Ovo je za dijelove (onaj sareniji graf); pokazuje dijelove koji se sumiraju
y0_L0 = []
y1_L1 = []
y2_L2 = []

for t in t_vals:
    clanovi = lagrange_clanovi(x_, y_, t)
    y0_L0.append(clanovi[0])
    y1_L1.append(clanovi[1])
    y2_L2.append(clanovi[2])

# Za usporedni graf
y0_L02 = []
y1_L12 = []
y2_L22 = []
y3_L32 = []

for t in t_vals:
    clanovi = lagrange_clanovi(x_2, y_2, t)
    y0_L02.append(clanovi[0])
    y1_L12.append(clanovi[1])
    y2_L22.append(clanovi[2])
    y3_L32.append(clanovi[3])

# Opet oni dijelovi
plt.plot(t_vals, y_lagrange, label="P2(t)", color="purple")
plt.plot(t_vals, y0_L0, label="x1·L1(t)", linestyle="--", color="pink")
plt.plot(t_vals, y1_L1, label="x2·L2(t)", linestyle="--", color="teal")
plt.plot(t_vals, y2_L2, label="x3·L3(t)", linestyle="--", color="grey")
plt.scatter(x_, y_, color="black", label="Tocke")
plt.title("Lagrangeovi clanovi interpolacije")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Opet oni dijelovi za cetvrtu tocku
plt.plot(t_vals, y_lagrange_2, label="P3(t)", color="purple")
plt.plot(t_vals, y0_L02, label="x1·L1(t)", linestyle="--", color="pink")
plt.plot(t_vals, y1_L12, label="x2·L2(t)", linestyle="--", color="teal")
plt.plot(t_vals, y2_L22, label="x3·L3(t)", linestyle="--", color="grey")
plt.plot(t_vals, y3_L32, label="x4·L4(t)", linestyle="--", color="blue")
plt.scatter(x_2, y_2, color="black", label="Tocke")
plt.title("Lagrangeovi clanovi interpolacije (4 tocke)")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

t_vals_full = [i * 0.1 for i in range(10, 51)]  # od 1.0 do 5.0
y_lagrange_full = [lagrange_interpolacija(x_, y_, t) for t in t_vals_full]
y_lagrange_2_full = [lagrange_interpolacija(x_2, y_2, t) for t in t_vals_full]
y_exact_full = [x_tocno(t) for t in t_vals_full]

# Full graf
plt.plot(t_vals_full, y_lagrange_full, label="P2(t)", color="pink")
plt.plot(t_vals_full, y_lagrange_2_full, label="P3(t)", color="teal")
plt.plot(t_vals_full, y_exact_full, label="x(t) analiticki", color="purple", linestyle="--")
plt.scatter(x_, y_, color="black", label="Tocke")
plt.title("Usporedba interpolacije i tocne funkcije")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Zadatci 5.2 i 5.3

# Ucitaj podatke
raw = np.loadtxt("V(H-H).txt")
r_ao = raw[:, 0]
V_hartree = raw[:, 1]

# Pretvorbe jedinica
AO_TO_A = 0.52917721092
HARTREE_TO_K = 315775.04
r_A = r_ao * AO_TO_A
V_K = V_hartree * HARTREE_TO_K

# Ukloni redove s NaN ili inf
mask_finite = np.isfinite(r_A) & np.isfinite(V_K) #maska koja je true za numeričke vrijednosti
r_A = r_A[mask_finite]
V_K = V_K[mask_finite]
order = np.argsort(r_A) #indeksi za sortiranje po ulaznome nizu
r_A = r_A[order]
V_K = V_K[order]


pd.DataFrame({"r[Å]": r_A, "V[K]": V_K}).to_csv("V(H-H)_AK.txt", sep="\t", index=False, float_format="%.6f")

# 71 tocka
x_vals_2 = np.linspace(2.81, 9.81, 71)

# Izracuni za Lagrange i Neville
yL_2 = [lagrange_interpolacija(r_A, V_K, x) for x in x_vals_2]
yp_2 = []
dyp_2 = []
for x in x_vals_2:
    val, err = polint.polint(r_A, V_K, len(r_A), x)
    yp_2.append(val)
    dyp_2.append(err)

df_inter = pd.DataFrame({
    "r[Å]": x_vals_2,
    "Lagrange": yL_2,
    "Neville": yp_2,
    "greska": dyp_2
})
df_inter.to_csv("V(H-H)_inter.txt", sep="\t", index=False, float_format="%.6f")

dyp_22 = []
for i in dyp_2:
    dyp_22.append(abs(i))


# Graf 2
plt.figure(figsize=(6.5, 4.0))
plt.scatter(r_A, V_K, color="black", label="(ri, Vi)")
plt.plot(x_vals_2, yL_2, "o", label="Lagrange", color="purple")
plt.errorbar(x_vals_2, yp_2, yerr=dyp_22, fmt="s", label="Neville", color="teal", ecolor="teal", capsize=1, linewidth = 1, markevery=2)
plt.xlabel("r / Å")
plt.ylabel("V / K")
plt.title("Graf 2")
plt.xlim(1.0, 10.0)
plt.ylim(-10.0, 10.0)
plt.grid(True)
plt.legend(loc="best")
plt.tight_layout()
plt.show()

# Graf usporedba s cubicspline
x_vals_3 = np.linspace(2.81, 9.81, 71)
yL_3 = [lagrange_interpolacija(r_A, V_K, x) for x in x_vals_3]
yp_3 = []
dyp_3 = []
for x in x_vals_3:
    val, err = polint.polint(r_A, V_K, len(r_A), x)
    yp_3.append(val)
    dyp_3.append(err)

cs = CubicSpline(r_A, V_K, bc_type="natural")
ys_3 = cs(x_vals_3)

dyp_32 = []
for i in dyp_3:
    dyp_32.append(abs(i))

# Dopuna datoteke
df_inter["Spline"] = cs(x_vals_3)
df_inter["Neville-Spline"] = df_inter["Neville"] - df_inter["Spline"]
df_inter.to_csv("V(H-H)_inter.txt", sep="\t", index=False, float_format="%.6f")


# Graf 3
plt.figure(figsize=(6.5, 4.0))
plt.scatter(r_A, V_K, color="black", label="(ri, Vi)")
plt.plot(x_vals_3, yL_3, "o", label="Lagrange", color="purple")
plt.errorbar(x_vals_3, yp_3, yerr=dyp_32, fmt="s", label="Neville", color="teal", ecolor="teal", capsize=1, linewidth = 1, markevery=2)
plt.plot(x_vals_3, ys_3, label="CubicSpline", color="pink")
plt.xlabel("r / Å")
plt.ylabel("V / K")
plt.title("Graf 3")
plt.xlim(1.0, 10.0)
plt.ylim(-10.0, 10.0)
plt.grid(True)
plt.legend(loc="best")
plt.tight_layout()
plt.show()