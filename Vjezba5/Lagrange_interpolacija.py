import matplotlib.pyplot as plt

# Funkcija koja racuna interpolacijski polinom u tocki x
def lagrange_interpolacija(x_, y_, x):
    n = len(x_)
    P = 0
    for i in range(n):
        L = 1
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
        L = 1
        for j in range(n):
            if j != i:
                L *= (x - x_[j]) / (x_[i] - x_[j])
        clanovi.append(y_[i] * L)
    return clanovi

# Tocna funkcija iz file-a
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