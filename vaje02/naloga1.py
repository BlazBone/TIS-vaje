from itertools import count
import collections
from math import log2

# from nis import match
from typing import Counter


def crkeFun(besedilo):
    H = 0
    a = Counter(str(besedilo))
    vse_crke = sorted(a)
    # b = {}
    for crka in vse_crke:
        H -= a[crka]/len(besedilo)*log2(a[crka]/len(besedilo))
    return H


def pariFun(besedilo):
    H1 = crkeFun(besedilo=besedilo)
    H2 = 0
    triplets = collections.defaultdict(int)
    posamezno = list(besedilo)
    for a, b in zip(posamezno[::], posamezno[1:]):
        triplets[a+b] += 1
    dolzina = sum(triplets.values())
    for a in triplets.values():
        H2 += (a/dolzina)*log2(dolzina/a)
    # print(H2)
    return H2 - H1


def trojkeFun(besedilo):
    H1 = crkeFun(besedilo)
    H2 = pariFun(besedilo=besedilo)
    trojcki = collections.defaultdict(int)
    for i, j, k in zip(besedilo, besedilo[1:], besedilo[2:]):
        trojcki[i + j + k] += 1

    st_vseh_trojckov = sum(trojcki.values())

    H3 = 0
    for val in trojcki.values():
        H3 += (val / st_vseh_trojckov) * log2(st_vseh_trojckov / val)
    # print("H3", H3)
    # print(H1, H2+H1, H3)
    return H3 - H2 - H1


# def trojkeFun(besedilo):
#     H1 = crkeFun(besedilo)
#     H2 = pariFun(besedilo=besedilo)
#     posamezno = list(besedilo)
#     H3 = 0
#     trojke = list(zip(posamezno[::], posamezno[1:], posamezno[2:]))

#     for a, b, c in set(trojke):
#         H3 -= (besedilo.count(a+b+c)/len(trojke)) * \
#             log2(besedilo.count(a+b+c)/len(trojke))
#     print("h1 h2 h3 ")
#     print(H1, H2 + H1, H3)
#     return H3-H2-H1

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
    besedilo = "".join(filter(lambda a: a.isalpha(), besedilo)).upper()
    H = 0
    if p == 0:
        H = crkeFun(besedilo=besedilo)
    elif p == 1:
        H = pariFun(besedilo=besedilo)
    elif p == 2:
        H = trojkeFun(besedilo=besedilo)

    return H
