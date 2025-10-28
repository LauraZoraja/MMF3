a = [0, -2, -2, -2]       # Donja dijagonala (a1 = 0 jer nema prethodnog retka)
b = [4, 6, 6, 8]          # Glavna dijagonala
c = [-2, -2, -2, 0]       # Gornja dijagonala (c4 = 0 jer nema sljedećeg retka)
d = [5, 0, 0, 0]          # Slobodni članovi (desna strana sustava)

n = len(d)  # Broj jednadzbi

# Pomocni nizova: c_ i d_ su modificirani koeficijenti, x su rješenja
c_ = [0.0] * n  # c″ u pdf-u: nova gornja dijagonala
d_ = [0.0] * n  # d″ u pdf-u: nova desna strana
x  = [0.0] * n  # Rjesenja

# Normalizacija prvog retka: dijelimo prvi redak tako da b1 postane 1
b[0] = b[0] / b[0] 
c_[0] = c[0] / b[0]
d_[0] = d[0] / b[0]

# Eliminacija elemenata ispod glavne dijagonale (forward sweep)
for i in range(1, n):
    naziv = b[i] - a[i] * c_[i - 1]  # Nazivnik za ažuriranje
    c_[i] = c[i] / naziv  # Gorjna dijagonala
    d_[i] = (d[i] - a[i] * d_[i - 1]) / naziv  # Desna strana jednakosti

# Rješavanje unatrag (back substitution): krećemo od zadnje jednadžbe jer tu imamo samo jedan nenulti koeficijent,
# a znamo zadnje rješenje
x[n - 1] = d_[n - 1] 

# Svako prethodno rješenje ovisi onome koji ga slijedi
for i in range(n - 2, -1, -1):
    x[i] = d_[i] - c_[i] * x[i + 1]

# Print
print("Rješenja struja I1, I2, I3, I4 su:")
for i, val in enumerate(x, start=1):
    print(f"I{i} = {val:.3f} A")
