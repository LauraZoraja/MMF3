import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# parametri
y01, A, B = 5.0, 1.0, 3.0
y02, C, D = 0.325, 2.0, 0.5

# komentar koji će biti pohranjen u datoteku
komentar = "Ovo je fiksni komentar upisan direktno u kod prije izvođenja."

def f1(t):
    return y01 + A*math.cos(B*t)

def f2(t):
    return y02 + C*math.exp(D*t)

def df1(t):
    return -A*B*math.sin(B*t)

def df2(t):
    return C*D*math.exp(D*t)

def f(t):
    return f1(t) - f2(t)

def df(t):
    return df1(t) - df2(t)

# Bisection with logging (use variable name 'output')
def bisekcija(a, b, tol=10**(-6), Nmax=200):
    output = []
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("preduvjeti nisu zadovoljeni: f(a) i f(b) moraju imati suprotne znakove")
    for i in range(1, Nmax+1):
        c = 0.5 * (a + b)
        fc = f(c)
        output.append({"iter": i, "c": c, "f(c)": fc})
        if abs(fc) < tol or (b - a)*0.5 < tol:
            return c, i, pd.DataFrame(output)
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return 0.5*(a+b), Nmax, pd.DataFrame(output)

# Newton-Raphson with logging (use variable name 'output')
def newton(x0, tol=10**(-10), Nmax=100):
    output = []
    x = x0
    for i in range(1, Nmax + 1):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 10**(-16):
            raise ValueError("Derivacija premala")
        xnew = x - fx/dfx
        output.append({"iter": i, "x_new": xnew, "f(x)": fx, "f'(x)": dfx})
        if abs(xnew - x) < tol:
            return xnew, i, pd.DataFrame(output)
        x = xnew
    return x, Nmax, pd.DataFrame(output)

# izvršavanje
t_bis, iter_bis, df_bis = bisekcija(2.0, 2.2, tol=1e-12)
t_newt, iter_newt, df_newt = newton(2.1, tol=1e-12)

y_at_t_bis = y01 + A*math.cos(B*t_bis)
y_at_t_newt = y01 + A*math.cos(B*t_newt)

diff_bis = abs(f1(t_bis) - f2(t_bis))
diff_newt = abs(f1(t_newt) - f2(t_newt))

# priprema sažetka kao DataFrame
summary = {
    "method": ["bisekcija", "newton"],
    "t": [t_bis, t_newt],
    "iterations": [iter_bis, iter_newt],
    "y1_minus_y2": [diff_bis, diff_newt],
    "y_at_t": [y_at_t_bis, y_at_t_newt]
}
df_summary = pd.DataFrame(summary)

# zapis u txt koristeći pandas (tab-separated), bez znanstvene notacije
filename = "rezultati_nultocke.txt"

with open(filename, "a", encoding="utf-8") as f:
    f.write("Rezultati pokusa\n")
    f.write(f"Parametri: y01={y01}, A={A}, B={B}, y02={y02}, C={C}, D={D}\n\n")
    f.write("Bisekcija iteracije (iter, c, f(c))\n")
    df_bis.to_csv(f, sep='\t', index=False, float_format="%.12f")
    f.write("\nNewton iteracije (iter, x_new, f(x), f'(x))\n")
    df_newt.to_csv(f, sep='\t', index=False, float_format="%.12f")
    f.write("\nSažetak\n")
    df_summary.to_csv(f, sep='\t', index=False, float_format="%.12f")
    f.write("\n")
    f.write(komentar + "\n")

# kratki ispis za informaciju
print(df_summary.to_string(index=False, float_format="%.12f"))

#plot
t_vals = np.linspace(-1, 3, 500)
f1_vals = [f1(t) for t in t_vals]
f2_vals = [f2(t) for t in t_vals]

plt.figure(figsize=(8, 5))
plt.plot(t_vals, f1_vals, label=r"$f_1(t) = y_{01} + A\cos(Bt)$", linewidth=2)
plt.plot(t_vals, f2_vals, label=r"$f_2(t) = y_{02} + C e^{Dt}$", linewidth=2)

# označi točke sjecišta
plt.scatter(t_bis, y_at_t_bis, color="red", s=70, zorder=5, label="Bisekcija sjecište")
plt.scatter(t_newt, y_at_t_newt, color="green", s=70, zorder=5, label="Newton sjecište")

# dodaj oznake
plt.text(t_bis, y_at_t_bis + 0.2, f"({t_bis:.3f}, {y_at_t_bis:.3f})", color="red", ha="center")
plt.text(t_newt, y_at_t_newt - 0.4, f"({t_newt:.3f}, {y_at_t_newt:.3f})", color="green", ha="center")

# izgled grafa
plt.xlabel("t")
plt.ylabel("y")
plt.title("Funkcije f1(t) i f2(t) i njihove nultočke (sjecišta)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()