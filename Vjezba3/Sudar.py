import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Parametri
y01, A, B = 5.0, 1.0, 3.0
y02, C, D = 0.325, 2.0, 0.5

#Funckije

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

#Bisekcija
def bisekcija(a, b, tol=10**(-12), Nmax=200):
    output = []
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("preduvjeti nisu zadovoljeni: f(a) i f(b) moraju imati suprotne znakove")
    for i in range(1, Nmax+1):
        c = 0.5 * (a + b)
        fc = f(c)
        output.append({"iteracija": i, "c": c, "f(c)": fc})
        if abs(fc) < tol or (b - a)*0.5 < tol:
            c = c, i = i
        elif fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return c, Nmax, pd.DataFrame(output)

# Newton-Raphson
def newton(x0, tol=10**(-12), Nmax=100):
    output = []
    x = x0
    for i in range(1, Nmax + 1):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 10**(-16):
            raise ValueError("Derivacija premala")
        xnew = x - fx/dfx
        output.append({"iteracija": i, "x_new": xnew, "f(x)": fx, "f'(x)": dfx})
        if abs(xnew - x) < tol:
            return xnew, i, pd.DataFrame(output)
        x = xnew
    return x, Nmax, pd.DataFrame(output)

#Pozivanje
t_bis, iter_bis, df_bis = bisekcija(2.0, 2.2, tol=10**(-12))
t_newt, iter_newt, df_newt = newton(2.1, tol=10**(-12))

y_at_t_bis = y01 + A*math.cos(B*t_bis)
y_at_t_newt = y01 + A*math.cos(B*t_newt)

diff_bis = abs(f1(t_bis) - f2(t_bis))
diff_newt = abs(f1(t_newt) - f2(t_newt))

#Priprema za ispis
summary = {
    "metoda": ["bisekcija", "newton"],
    "t": [t_bis, t_newt],
    "iteracije": [iter_bis, iter_newt],
    "y1 - y2": [diff_bis, diff_newt],
    "y(t)": [y_at_t_bis, y_at_t_newt]
}
df_summary = pd.DataFrame(summary)

#Zapis u txt
filename = "rezultati_nultocke.txt"

komentar = "Vidimo da je Newton-Raphson metoda povoljnija što se tiče broja iteracija, a obje naposlijetku davaju jednak rezultat."

with open(filename, "a", encoding="utf-8") as f:
    f.write("Rezultati\n")
    f.write(f"Parametri: y01={y01}, A={A}, B={B}, y02={y02}, C={C}, D={D}\n\n")
    f.write("Bisekcija iteracije (iteracija, c, f(c))\n")
    df_bis.to_csv(f, sep='\t', index=False, float_format="%.12f")
    f.write("\nNewton iteracije (iteracija, x_new, f(x), f'(x))\n")
    df_newt.to_csv(f, sep='\t', index=False, float_format="%.12f")
    f.write("\nSažetak\n")
    df_summary.to_csv(f, sep='\t', index=False, float_format="%.12f")
    f.write("\n")
    f.write(komentar + "\n")

print(df_summary.to_string(index=False, float_format="%.12f"))

#plot
t_vals = np.linspace(-1, 3, 500)
f1_vals = [f1(t) for t in t_vals]
f2_vals = [f2(t) for t in t_vals]

plt.figure(figsize=(8, 5))
plt.plot(t_vals, f1_vals, label=r"$f_1(t) = y_{01} + A\cos(Bt)$", linewidth=2, color="purple")
plt.plot(t_vals, f2_vals, label=r"$f_2(t) = y_{02} + C e^{Dt}$", linewidth=2, color="pink")

#sjecišta koristeći metode
plt.scatter(t_bis, y_at_t_bis, color="teal", s=70, label="Bisekcija sjecište")
plt.scatter(t_newt, y_at_t_newt, color="black", s=70, label="Newton sjecište")

plt.text(t_bis, y_at_t_bis + 0.2, f"({t_bis:.3f}, {y_at_t_bis:.3f})", color="teal")
plt.text(t_newt, y_at_t_newt - 0.4, f"({t_newt:.3f}, {y_at_t_newt:.3f})", color="black")

# izgled grafa
plt.xlabel("t")
plt.ylabel("y")
plt.title("Funkcije f1(t) i f2(t) i njihovo sjecište")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()