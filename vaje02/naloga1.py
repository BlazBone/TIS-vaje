from itertools import count
from math import log2
# from nis import match
from typing import Counter


def crkeFun(besedilo):
    H = 0
    a = Counter(str(besedilo))
    vse_crke = sorted(a)
    b = {}
    for crka in vse_crke:
        b[crka] = a[crka]/len(besedilo)
        H -= b[crka]*log2(b[crka])
    return H


def pariFun(besedilo):
    H1 = crkeFun(besedilo=besedilo)
    H2 = 0

    posamezno = list(besedilo)
    pari = list(zip(posamezno[:-1], posamezno[1:]))
    verjetnost_dvojckov = {}
    for a, b in set(pari):
        verjetnost_dvojckov[a+b] = besedilo.count(a+b)/len(pari)
        H2 -= verjetnost_dvojckov[a+b] * log2(verjetnost_dvojckov[a+b])
    return H2 - H1


def trojkeFun(besedilo):
    H1 = crkeFun(besedilo)
    H2 = pariFun(besedilo=besedilo)
    posamezno = list(besedilo)
    H3 = 0
    verjetnost_trojk = {}
    trojke = list(zip(posamezno[:-2], posamezno[1:-1], posamezno[2:]))
    print(trojke[:11])
    print(len(trojke))
    print(len(set(trojke)))

    for a, b, c in set(trojke):
        verjetnost_trojk[a+b+c] = besedilo.count(a+b+c)/len(trojke)
        H3 -= verjetnost_trojk[a+b+c]*log2(verjetnost_trojk[a+b+c])

    return H3-H2-H1


def naloga1(besedilo, p):
    """ Izracun povprecne nedolocenosti na znak
     1.odstrani vse razn crk angleske abecede
    2. spremeni 'case' Tako da bodo use crke majhne ali velike
    Parameters
    ----------
    besedilo : str
        Vhodni niz
    p : int
        Stevilo poznanih predhodnih znakov: 0, 1 ali 2.
        p = 0: H(X1)
            racunamo povprecno informacijo na znak abecede
            brez poznanih predhodnih znakov
        p = 1: H(X2|X1)
            racunamo povprecno informacijo na znak abecede
            pri enem poznanem predhodnemu znaku
        p = 2: H(X3|X1,X2)
    Returns
    -------
    H : float
        Povprecna informacija na znak abecede z upostevanjem
        stevila poznanih predhodnih znakov 'p'
    """
    besedilo = "".join(filter(lambda a: a.isalpha(), besedilo)).lower()
    H = 0
    if p == 0:
        H = crkeFun(besedilo=besedilo)
    elif p == 1:
        H = pariFun(besedilo=besedilo)
    elif p == 2:
        H = trojkeFun(besedilo=besedilo)

    return H
