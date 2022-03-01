from math import log2
from nis import match
from typing import Counter


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
    besedilo = besedilo.strip().replace(".", '').replace(',', '').replace(
        ";", '').lower().replace("'", "").replace(":", '').replace("?", '').replace(" ", '').replace("-", '').replace('(', '').replace(')', '').replace("!", '')
    text_len = len(besedilo)

    a = Counter(str(besedilo))
    vse_crke = sorted(a)
    print(vse_crke)
    if p == 1:
        b  = {}
        print("1")
        H = 0
        for crka in vse_crke:
            b[crka] = a[crka]/text_len
            H -= b[crka]*log2(b[crka])
    elif p == 2:
        b1 = {}
        for crka in vse_crke:
            b1[crka] = a[crka]/text_len
        print('2')
        
    elif p == 3:
        print("3")

    print(H)
    return H
