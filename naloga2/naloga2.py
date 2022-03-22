def naloga2(vhod: list, nacin: int) -> tuple[list, float]:
    # slovar = {}
    # for i in range(256):
    # print(i)
    # slovar[chr(i)] = i
    MAX_SIZE_SLOVAR = 4096
    izhod = []
    if nacin == 0:
        slovar = dict([(chr(x), x) for x in range(256)])

        N = ''
        inte = 256
        for crka in vhod:
            # print(index, crka)
            if N+crka in slovar:
                N = N+crka
            else:
                izhod.append(slovar[N])
                if len(slovar) < MAX_SIZE_SLOVAR:
                    slovar[N+crka] = inte
                    inte += 1
                N = crka

        izhod.append(slovar[N])
        R = (len(izhod)*12)/(len(vhod)*8)

    else:
        slovar = dict([(x, chr(x)) for x in range(256)])
        K = ''
        inte = 256
        N = ''
        for index, koda in enumerate(vhod):
            # koda = str(koda)
            # if index % 500 == 0:
            #     print(koda)
            if index == 0:
                N = slovar[koda]
                izhod.append(N)
                K = N
            else:
                if koda in slovar:
                    N = slovar[koda]
                else:
                    N = K+K[0]
                izhod.extend(list(N))
                if len(slovar) < MAX_SIZE_SLOVAR:
                    slovar[inte] = K+N[0]
                    inte += 1
                K = N

        R = (len(vhod)*12)/(len(izhod)*8)

    return (izhod, R)
