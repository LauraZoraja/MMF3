import numpy as np

a = [0, -2, -2, -2]       # Donja dijagonala
b = [4, 6, 6, 8]          # Glavna dijagonala
c = [-2, -2, -2, 0]       # Gornja dijagonala
d = [5, 0, 0, 0]          # Slobodni clanovi

n = len(d) # Broj jednadzbi i nepoznanica

# Pomocni nizovi
c_ = [0.0] * n
d_ = [0.0] * n
x  = [0.0] * n

# Thomasov algoritam
c_[0] = c[0] / b[0]
d_[0] = d[0] / b[0] # Ove dvije linije potrebne su za normalizaciju prvog reda

for i in range(1, n): # Eliminacija donje dijagonale
    denom = b[i] - a[i] * c_[i - 1]
    c_[i] = c[i] / denom if i < n - 1 else 0 # Azuriran gornji koeficijent
    d_[i] = (d[i] - a[i] * d_[i - 1]) / denom # Azuriran slobodni clan

# Rjesavanje
x[n - 1] = d_[n - 1] # Rjesenje za posljednju nepoznanicu koju znamo direktno iz proslog dijela
for i in range(n - 2, -1, -1):
    x[i] = d_[i] - c_[i] * x[i + 1] # Prethodne nepoznanice racunamo poznavajuci sljedece

# Ispis rjesenja
print("Rjesenja struja I1, I2, I3, I4 su:")
for i, val in enumerate(x, start=1):
    print(f"I{i} = {val:.3f} A")

print("94*I_{1,2,3,4}:")
for i, val in enumerate(x, start=1):
    scaled = 94 * val
    print(f"I{i} = {scaled:.3f} A")

# Provjera A*x = d
A = np.zeros((n, n))
for i in range(n):
    A[i][i] = b[i]
    if i > 0:
        A[i][i - 1] = a[i]
    if i < n - 1:
        A[i][i + 1] = c[i]

x_vec = np.array(x)
d_vec = np.array(d)
Ax = A @ x_vec # Matricno mnozenje
if np.allclose(Ax, d_vec): # Provjera jednakosti s tolerancijom, gotova funkcija nađena online, np.array_equal() za tocna podudaranja
    print("Provjera A*x = d je uspjesna.")
else:
    print("Provjera A*x = d nije uspjesna.")

# Provjera A*A^-1 = I
A_inv = np.linalg.inv(A)
AA_inv = A @ A_inv
I = np.eye(n) # Naredba koja stvara jedinicnu matricu dimenzije n x n
if np.allclose(AA_inv, I):
    print("Provjera A*A^{-1} je uspjesna.")
else:
    print("Provjera A*A^{-1} nije uspjesna.")


# Spremanje u datoteku
with open("rjesenja.txt", "w") as f:
    f.write("Rjesenja struja I1, I2, I3, I4:\n")
    for i, val in enumerate(x, start=1):
        f.write(f"I{i} = {val:.6f} A\n")
    f.write("\n94*I_{1,2,3,4}:\n")
    for i, val in enumerate(x, start=1):
        scaled = 94 * val
        f.write(f"I{i} = {scaled:.6f} A\n")
    f.write("\nProvjera A*x = d:\n")
    for i in range(n):
        f.write(f"A*x[{i+1}] = {Ax[i]:.6f}, ocekivano d[{i+1}] = {d[i]:.6f}\n")
    f.write("\nProvjera A*A^{-1} = I:\n")
    f.write(str(AA_inv))

print("\nProvjere i rjesenja su pohranjeni u datoteku 'rjesenja.txt'.")
