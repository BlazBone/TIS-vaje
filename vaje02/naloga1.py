from math import log2
from typing import Counter


def crkeFun(besedilo):
    H = 0
    a = Counter(besedilo)
    for crka in a.values():
        H -= crka/len(besedilo)*log2(crka/len(besedilo))
    return H


def pariFun(besedilo):
    H1 = crkeFun(besedilo=besedilo)
    H2 = 0
    posamezno = list(besedilo)
    num_repetitions = Counter(zip(posamezno, posamezno[1:]))
    stevilo_vseh = sum(num_repetitions.values())
    for a in num_repetitions.values():
        H2 += (a/stevilo_vseh)*log2(stevilo_vseh/a)
    return H2 - H1


def trojkeFun(besedilo):
    H1 = crkeFun(besedilo)
    H2 = pariFun(besedilo=besedilo)
    posamezno = list(besedilo)
    num_repetitions = Counter(zip(posamezno, posamezno[1:], posamezno[2:]))
    st_vseh_trojckov = sum(num_repetitions.values())
    H3 = 0
    for val in num_repetitions.values():
        H3 += (val / st_vseh_trojckov) * log2(st_vseh_trojckov / val)
    return H3 - H2 - H1


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
