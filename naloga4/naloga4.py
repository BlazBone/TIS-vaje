import numpy as np

def naloga4(vhod,fs):
    """
    Poisce akord v zvocnem zapisu.

    Parameters
    ----------
    vhod : list
        vhodni zvocni zapis 
    fs : int
        frekvenca vzorcenja
    
    Returns
    -------
    izhod : str
        ime akorda, ki se skriva v zvocnem zapisu;
        ce frekvence v zvocnem zapisu ne ustrezajo nobenemu od navedenih akordov, 
        vrnemo prazen niz ''
    """
    ###########################################################################
    N = len(vhod)
    f = np.arange(0,N) * (fs/N) #frekvencna os
    #DFT
    f = np.arange(0,N) * (fs/N) #frekvencna os
    #DFT
    x = vhod
    X = np.fft.fft(x)

    #mocnosti spekter
    P = np.square( np.abs(X)) /N

    tones = {'C1':261.63, 'CIS1':277.18, 'D1':293.66, 'DIS1':311.13,'E1':329.63,'F1':349.23, 'FIS1':369.99, 'G1':392, 'GIS1':415.30,'A1':440,'B1':466.16,'H1':493.88,
             'C2':523.25,'CIS2':554.37,'D2':587.33,'DIS2':622.25,'E2':659.25,'F2':698.46,'FIS2':739.99,'G2':783.99,'GIS2':830.61,'A2':880,'B2':932.33,'H2':987.77 }
    accords = {'Cdur':"C1E1G1",'Cmol':'C1DIS1G1','Ddur':'D1FIS1A1','Dmol':'D1F1A1','Edur':'E1GIS1H1','Emol':'E1G1H1','Fdur':'F1A1C2','Fmol':'F1GIS1C2'
               ,'Gdur':'G1H1D2','Gmol':'G1B1D2','Amol':'A1C2E2','Adur':'A1CIS2E2','Hmol':'H1D2FIS2','Hdur':'H1DIS2FIS2'}

    nparr = np.array(P)
    novp = nparr/np.max(nparr)
    freqTonov = []
    for index,size in enumerate(novp):
        if index > len(P)/2:
            break
        if size > 0.01:
            freq = index * (fs/N)
            freqTonov.append(freq) 
    
    end_tones = []
    for frq in freqTonov:
        for key,value in tones.items():
            if abs(frq-value) < 1:
                end_tones.append(key)
                
                    
        
    end_tones = list(dict.fromkeys(end_tones))
    together = ""
    if len(end_tones) <= 5:
        for tone in end_tones[0:3:1]:
            together += tone
    elif len(end_tones) == 6:
        togetherNizji = ""
        togehter1 = ""
        togehter2 = ""
        for tone in end_tones:
            if tone[len(tone)-1] == '1':
                togetherNizji += tone
                togehter1+=tone[:len(tone)-1]
            elif tone[len(tone)-1] == '2':
                togehter2+=tone[:len(tone)-1]
        if togetherNizji in accords.values() and togehter1 == togehter2:
            together = togetherNizji
    
            
    izhod = ''
    for acc,tons in accords.items():
        if tons == together:
            izhod = acc
     
    return izhod