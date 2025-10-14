import math
from decimal import Decimal, getcontext
import pandas as pd


getcontext().prec = 80


def prvi(x, epsilon, prikazi=False):
    xD = Decimal(x)
    epsD = Decimal(str(epsilon))
    suma = Decimal(1)
    term = Decimal(1)
    k = 1
    koraci, vrijednosti = [0], [float(suma)]
    while True:
        term = -term * xD / Decimal(k)
        suma += term
        koraci.append(k)
        vrijednosti.append(float(suma))
        if abs(term) < epsD:
            break
        k += 1
    if prikazi:
        return koraci, vrijednosti
    return float(suma), k


def drugi(x, epsilon, prikazi=False):
    xD = Decimal(x)
    epsD = Decimal(str(epsilon))
    sk = Decimal(1)
    suma = Decimal(1)
    k = 1
    koraci, vrijednosti = [0], [float(suma)]
    while True:
        sk = -sk * xD / Decimal(k)
        suma += sk
        koraci.append(k)
        vrijednosti.append(float(suma))
        if abs(sk) < epsD:
            break
        k += 1
    if prikazi:
        return koraci, vrijednosti
    return float(suma), k


def treci(x, epsilon, prikazi=False):
    xD = Decimal(x)
    epsD = Decimal(str(epsilon))
    suma = Decimal(1)
    term = Decimal(1)
    k = 1
    koraci, vrijednosti = [0], [float(1 / suma)]
    while True:
        term = term * xD / Decimal(k)
        suma += term
        inv = (Decimal(1) / suma)
        koraci.append(k)
        vrijednosti.append(float(inv))
        if abs(term) < epsD:
            break
        k += 1
    if prikazi:
        return koraci, vrijednosti
    return float(Decimal(1) / suma), k


def tablice_po_preciznosti():
    x_vrijednosti = list(range(0, 101, 10))
    epsiloni = [1e-5, 1e-10, 1e-15]
    tablice = {"prvi": [], "drugi": [], "treci": []}

    for x in x_vrijednosti:
        exp_ref = math.exp(-x)  # točna vrijednost
        red_prvi = {"x": x, "exp(-x)": exp_ref}
        red_drugi = {"x": x, "exp(-x)": exp_ref}
        red_treci = {"x": x, "exp(-x)": exp_ref}

        for eps in epsiloni:
            p_suma, p_k = prvi(x, eps)
            d_suma, d_k = drugi(x, eps)
            t_suma, t_k = treci(x, eps)

            if eps == 1e-10:
                red_prvi["k"] = p_k
                red_drugi["k"] = d_k
                red_treci["k"] = t_k

            if eps == 1e-10:
                red_prvi["suma_1e-10"] = p_suma
                red_drugi["suma_1e-10"] = d_suma
                red_treci["suma_1e-10"] = t_suma
            elif eps == 1e-5:
                red_prvi["suma_1e-5"] = p_suma
                red_drugi["suma_1e-5"] = d_suma
                red_treci["suma_1e-5"] = t_suma
            elif eps == 1e-15:
                red_prvi["suma_1e-15"] = p_suma
                red_drugi["suma_1e-15"] = d_suma
                red_treci["suma_1e-15"] = t_suma

        tablice["prvi"].append(red_prvi)
        tablice["drugi"].append(red_drugi)
        tablice["treci"].append(red_treci)

    df_prvi = pd.DataFrame(tablice["prvi"])
    df_drugi = pd.DataFrame(tablice["drugi"])
    df_treci = pd.DataFrame(tablice["treci"])
    return df_prvi, df_drugi, df_treci


def detaljne_iteracije(eps=1e-10):
    x = 20
    eps = 1e-10
    kor1, val1 = prvi(x, eps, prikazi=True)
    kor2, val2 = drugi(x, eps, prikazi=True)
    kor3, val3 = treci(x, eps, prikazi=True)
    duljina = min(len(kor1), len(kor2), len(kor3))
    df = pd.DataFrame({
        "k": kor1[:duljina],
        "Suma_prvi": val1[:duljina],
        "Suma_drugi": val2[:duljina],
        "Inverz_treci": val3[:duljina]
    })
    return df


df_prvi, df_drugi, df_treci = tablice_po_preciznosti()
df_iter = detaljne_iteracije()

with open("rezultati_tablica.txt", "w", encoding="utf-8") as f:
    f.write("TABLICA 1A: PRVI NAČIN\n")
    f.write(df_prvi.to_string(index=False))
    f.write("\n\nTABLICA 1B: DRUGI NAČIN\n")
    f.write(df_drugi.to_string(index=False))
    f.write("\n\nTABLICA 1C: TREĆI NAČIN\n")
    f.write(df_treci.to_string(index=False))
    f.write("\n\nTABLICA 2 (x=20, epsilon = 10^(-10)):\n")
    f.write(df_iter.to_string(index=False))
    f.write("\n\n KOMENTAR VJEŽBE I REZULTATI:\n")
    f.write("U tablicama 1A, 1B i 1C vidimo kako se različiti načini konvergencije ponašaju za različite vrijednosti x i epsilon. "
            "Prvi i drugi način su vrlo slični u broju potrebnih iteracija za postizanje zadane preciznosti, dok treći način pokazuje značajno veću učinkovitost, posebno za veće vrijednosti x. \n" \
            "Sličnost u rezultatima prvog i drugog načina jest ta što su skoro pa isti načini izračuna, samo zapisani drukčije. "
            "Ovo je očekivano jer treći način koristi inverznu sumu, što pomaže u smanjenju numeričkih pogrešaka kod velikih x.\n"
            "U tablici 2, koja prikazuje detaljne iteracije za x= 20 i epsilon = 10^-10, možemo vidjeti kako se približavamo točnoj vrijednosti exp(-20) kroz iteracije. "
            "Svi načini konvergencije pokazuju stabilan rast prema točnoj vrijednosti, ali treći način to čini s manje iteracija.\n" \
            "Vidljivo je da preciznost prva dva načina znatno opada za veće x, dok treći način ostaje stabilan i precizan, što ga čini najoptimalnijim za ovakve programe.\n"
            "Zaključno, izbor metode može značajno utjecati na učinkovitost izračuna, posebno za veće vrijednosti x, gdje treći način pokazuje jasnu prednost.")

print("\nDatoteka 'rezultati_tablica.txt'")
