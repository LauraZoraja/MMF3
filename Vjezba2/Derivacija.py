import numpy as np
import pandas as pd 
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

output = []

# Prva derivacija
x_vals_1st = [0.5, 1.5, 2.5]
h_vals = [10**(-1), 10**(-4), 10**(-6)]

print("Prva derivacija f(x) = e^x")
output.append("Prva derivacija f(x) = e^x")
for x in x_vals_1st:
    rows1 = []
    for h in h_vals:
        exact = df_exact(x)
        row1 = [
            h,
            exact,
            forward_diff(f, x, h),
            backward_diff(f, x, h),
            central_diff(f, x, h)
        ]
        rows1.append(row1)
    df1 = pd.DataFrame(rows1, columns=['h', 'Točna vrijednost', 'Unaprijed', 'Unatrag', 'Centralna'])
    print(f"\nTablica 1 za x = {x}")
    output.append(f"\nTablica 1 za x = {x}")
    print(df1.to_string(index=False))
    output.append(df1.to_string(index=False))


for x in x_vals_1st:
    rows2 = []
    for h in h_vals:
        exact = df_exact(x)
        row2 = [
            h,
            exact,
            central_diff(f, x, h),
            three_point_diff(f, x, h),
            five_point_diff(f, x, h)
        ]
        rows2.append(row2)
    df2 = pd.DataFrame(rows2, columns=['h', 'Točna vrijednost', 'Dvije točke', 'Tri točke', 'Pet točki'])
    print(f"\nTablica 2 za x = {x}")
    output.append(f"\nTablica 2 za x = {x}")
    print(df2.to_string(index=False))
    output.append(df2.to_string(index=False))

# Druga derivacija
x_vals_2nd = list(range(11))
h_vals_2nd = [10**(-1), 10**(-2), 10**(-3), 10**(-4), 10**(-5), 10**(-6)]

errors = {x: [] for x in [1, 5, 10]}

print("\nDruga derivacija f(x) = e^x")
output.append("\nDruga derivacija f(x) = e^x")
for x in x_vals_2nd:
    rows3 = []
    print(f"\nTablica 3 za x = {x}")
    output.append(f"\nTablica 3 za x = {x}")
    for h in h_vals_2nd:
        exact = d2f_exact(x)
        numeric = second_derivative(f, x, h)
        error = abs(numeric - exact)
        row3 = [h, exact, numeric, error]
        rows3.append(row3)
        if x in errors:
            errors[x].append(error)
    df3 = pd.DataFrame(rows3, columns=['h', 'Točna vrijednost', 'Numerička vrijednost', 'Greška'])
    print(df3.to_string(index=False))
    output.append(df3.to_string(index=False))

with open("tablice_derivacija.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output))

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

komentar = " \n U tablicama 1 vidljivo je da manji h i centralna derivacija vraćaju najprecizniji rezultat.\n" \
"To nije iznenađujuće, obzirom da centralna derivacija koristi informacije s obje strane točke, \n" \
"što rezultira boljom aproksimacijom. U tablicama 2, pet točaka daje najbolju preciznost zbog \n" \
"šireg uzorka podataka koji koristi za izračun derivacije.\n" \
"Graf greške za drugu derivaciju pokazuje da se greška smanjuje kako h postaje manje, \n" \
"što je očekivano jer manji koraci vode do točnijih aproksimacija derivacija.\n" \
"Iznenađujuće je što greška ne opada linearno s smanjenjem h, već ima minimumalnu vrijednost \n" \
"nakon čega počinje rasti zbog numeričkih pogrešaka povezanim s ograničenom preciznošću računala. \n" \
"Da naš kompjuter ima beskonačnu preciznost, greška bi se nastavila smanjivati s manjim h."
print(komentar)
with open("tablice_derivacija.txt", "a", encoding="utf-8") as f:
    f.write("\n" + komentar + "\n")