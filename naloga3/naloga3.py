import numpy as np
from math import log2

def toInt(x: list):
    return int(''.join([str(x1 % 2) for x1 in x]), 2)

def toHex(vhod: list):
    num1 = 0
    num2 = 0
    crke = ['A', 'B', 'C', 'D', 'E', 'F']
    for index, bit in enumerate(vhod):
        if index < 4:
            num2 += bit * (2 ** index)
        else: 
            num1 += bit * (2 ** (index - 4))
    if num1 >= 10:
        num1 = crke[num1 - 10]
    
    if num2 >= 10:
        num2 = crke[num2 - 10]
    return str(num1) + str(num2)

def crc8(vhod: list):
    crc = 0
    register = [1 for x in range(8)]
    genpol = [0,1,0,1,1,0,0,1]
    for x in vhod:
        xor = x ^ register[7]
        if xor :
            register.insert(0, 1)
            register.pop()
            for i in range(8):
                register[i]=register[i]^genpol[i]                
        else:
            register.insert(0, 0)
            register.pop()
    
    return register

def naloga3(vhod: list, n: int):
    m = int(log2(n+1))
    k = n - m
    vhod = np.array(vhod)
    def get_bin(x, n): return format(x, 'b').zfill(n)
    vhodx = n
    vhody = len(vhod)//n
    inp = vhod.reshape(vhody, vhodx)
    
    
    vhodZaCrc = vhod[::]
    crclist = crc8(vhodZaCrc)
    crc = toHex(crclist)


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

    return (izhod, crc)
