import numpy as np
from math import log2

def toInt(x: list):
    return int(''.join([str(x1 % 2) for x1 in x]), 2)

def naloga3(vhod: list, n: int):
    m = int(log2(n+1))
    k = n - m
    vhod = np.array(vhod)
    def get_bin(x, n): return format(x, 'b').zfill(n)
    vhodx = n
    vhody = len(vhod)//n
    inp = vhod.reshape(vhody, vhodx)
    CRC = np.array([1 for x in range(8)])
    stPolnih = len(vhod)//8
    vhodZaCrc = vhod[::]
    i = 0
    while(i<stPolnih):
        CRC = np.array([toInt(x) for x in CRC])
        CRC = np.array([x ^ y for x, y in zip(CRC, inp[i])])
        i += 1


        
    stolpci = np.array(
        [x for x in range(n+1) if (x & (x - 1)) != 0])
    identitea = np.array([x for x in range(1, n+1) if (x & (x - 1)) == 0])
    stevilaPoVrsti = np.concatenate([stolpci, identitea])

    Ht = [[int(st) for st in get_bin(x, m)[::-1]] for x in stevilaPoVrsti]
    
    out = np.matmul(inp, Ht)
    izhod = []
    
    for index, sindrom in enumerate(out):
        # mesto = toInt(sindrom[::-1]) # deljajo vsi razn 3 test
        mesto = toInt(sindrom) # deljajo pou testu
        if mesto == 0:
            cas = np.array(inp[index, 0:k])
            izhod.extend(cas)
            continue
        for index2, stolpc in enumerate(stevilaPoVrsti):
            if stolpc == mesto:
                inp[index, index2] = (inp[index, index2] + 1) % 2
                cas = np.array(inp[index, 0:k])
                izhod.extend(cas)
                break

    crc = ''
    print("dolzina izhoda:, ", len(izhod))
   
    return (izhod, crc)
