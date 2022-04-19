import numpy as np
from math import log2


def toInt(x: list):
    return int(''.join([str(x1 % 2) for x1 in x]), 2)


def naloga3(vhod: list, n: int):
    """
    Izvedemo dekodiranje binarnega niza `vhod`, zakodiranega
    s Hammingovim kodom dolzine `n` in poslanega po zasumljenem kanalu.
    Nad `vhod` izracunamo vrednost `crc` po standardu CRC-8/CDMA2000.

    Parameters
    ----------
    vhod : list
        Sporocilo y, predstavljeno kot seznam bitov (stevil tipa int)
    n : int
        Stevilo bitov v kodni zamenjavi

    Returns
    -------
    (izhod, crc) : tuple[list, str]
        izhod : list
            Odkodirano sporocilo y (seznam bitov - stevil tipa int)
        crc : str
            Vrednost CRC, izracunana nad `vhod`. Niz dveh znakov.
    """

    m = int(log2(n+1))
    k = n - m
    vhod = np.array(vhod)
    def get_bin(x, n): return format(x, 'b').zfill(n)
    vhodx = n
    vhody = len(vhod)//n
    inp = vhod.reshape(vhody, vhodx)
    CRC = np.array([1 for x in range(8)])

    stPolnih = len(vhod)//8
    i = 0
    print(stPolnih)
    while(stPolnih > i):
        part = vhod[i*8:(i+1)*8]
        CRC = part + CRC
        i += 1

    print(CRC)
    # print(inp)

    stolpci = np.array(
        [x for x in range(n+1) if (x & (x - 1)) != 0])
    identitea = np.array([x for x in range(1, n+1) if (x & (x - 1)) == 0])
    stevilaPoVrsti = np.concatenate([stolpci, identitea])
    # print(stevilaPoVrsti)

    Ht = [[int(st) for st in get_bin(x, m)[::-1]] for x in stevilaPoVrsti]
    # print(Ht)

    out = np.matmul(inp, Ht)
    # izhod = np.array([0])
    # print(out)
    # print(out)
    izhod = []
    # print(stevilaPoVrsti)
    for index, sindrom in enumerate(out):
        mesto = toInt(sindrom)
        # print(sindrom, "->", mesto)
        if mesto == 0:
            cas = np.array(inp[index, 0:k])
            # izhod = izhod+cas
            izhod.extend(cas)
            # print(cas)
            continue
        for index2, stolpc in enumerate(stevilaPoVrsti):
            if stolpc == mesto:
                inp[index, index2] = (inp[index, index2] + 1) % 2
                cas = np.array(inp[index, 0:k])
                # print(cas)
                # izhod.append(cas)
                # izhod = izhod+cas
                izhod.extend(cas)

                break

    # print(out)
    # izhod = []
    # print(izhod, "hej")
    crc = ''
    return (izhod, crc)
