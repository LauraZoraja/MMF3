import numpy as np
import math
from decimal import Decimal
import pandas as pd

rezultati = {
    "x": [],
    "Prvi_nacin_suma": [],
    "Prvi_nacin_k": [],
    "Prvi_nacin_inverz": [],
    "Drugi_nacin_suma": [],
    "Drugi_nacin_k": [],
    "Drugi_nacin_inverz": [],
    "Treci_nacin_suma": [],
    "Treci_nacin_k": [],
    "Treci_nacin_inverz": []
}

# prvi nacin, preko reda
def prvi(x, epsilon, prikazi_clanove=False):
    suma = Decimal(1)
    k = Decimal(1)
    x = Decimal(x)
    clanovi, koraci = [], []

    while True:
        c = ((-x)**k) / math.factorial(int(k))
        c = Decimal(c)
        suma += c
        koraci.append(int(k))
        clanovi.append(float(suma))
        if abs(c) < epsilon:
            break
        k += 1

    rezultati["x"].append(float(x))
    rezultati["Prvi_nacin_suma"].append(float(suma))
    rezultati["Prvi_nacin_k"].append(float(k))
    rezultati["Prvi_nacin_inverz"].append(float(1/suma))

    if prikazi_clanove and x == 20:
        df = pd.DataFrame({'Iteracija': koraci, 'Vrijednost': clanovi})
        print("\nPrvi način (x=20):")
        print(df.to_string(index=False))


# drugi nacin, rekurzivna formula
def drugi(x, epsilon, prikazi_clanove=False):
    sk = Decimal(1)
    k = Decimal(1)
    suma = Decimal(1)
    x = Decimal(x)
    clanovi, koraci = [], []

    while True:
        sk = -sk * x / k
        suma += sk
        koraci.append(int(k))
        clanovi.append(float(suma))
        if abs(sk) < epsilon:
            break
        k += 1

    rezultati["Drugi_nacin_suma"].append(float(suma))
    rezultati["Drugi_nacin_k"].append(float(k))
    rezultati["Drugi_nacin_inverz"].append(float(1/suma))

    if prikazi_clanove and x == 20:
        df = pd.DataFrame({'Iteracija': koraci, 'Vrijednost': clanovi})
        print("\nDrugi način (x=20):")
        print(df.to_string(index=False))


# treci nacin, e^x pa inverz
def treci(x, epsilon, prikazi_clanove=False):
    suma = Decimal(1)
    k = Decimal(1)
    x = Decimal(x)
    clanovi, koraci = [], []

    while True:
        c = (x**k) / math.factorial(int(k))
        c = Decimal(c)
        suma += c
        koraci.append(int(k))
        clanovi.append(float(suma))
        if abs(c) < epsilon:
            break
        k += 1

    rezultati["Treci_nacin_suma"].append(float(suma))
    rezultati["Treci_nacin_k"].append(float(k))
    rezultati["Treci_nacin_inverz"].append(float(1/suma))

    if prikazi_clanove and x == 20:
        df = pd.DataFrame({'Iteracija': koraci, 'Vrijednost': clanovi})
        print("\nTreći način (x=20):")
        print(df.to_string(index=False))


# --- Glavni pozivi ---
print('Clanovi i koraci iteracije za x=20:')

prvi(20, 10**(-10), prikazi_clanove=True)
drugi(20, 10**(-10), prikazi_clanove=True)
treci(20, 10**(-10), prikazi_clanove=True)
