import numpy as np
from scipy.io.wavfile import write
from matplotlib import pyplot as plt
# def naloga4(vhod: list, fs: int) -> str:
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
    accords = {'Cdur':"C1E1G1",'Cmol':'C1DIS1G1','Ddur':'D1FIS1A1','Dmol':'D1F1A1','Edur':'E1GIS1H1','Fdur':'F1A1C2','Fmol':'F1GIS1C2'
               ,'Gdur':'G1H1D2','Gmol':'G1B1D2','Amol':'A1C2E2','Adur':'A1CIS2E2','Hmol':'H1D2FIS2','Hdur':'H1DIS2FIS2'}
    
    figure, axis = plt.subplots()
    # axis[0].plot(t,x, color='blue')
    # axis[0].set_title("jakost v odvisnosti od casa")
    # axis[0].set_xlabel("t[s]")
    print(P)
    axis.plot(f,P, color='red')
    axis.set_title("moc v  odvisnosti od frekvence")
    axis.set_xlabel("f[Hz]")
    # plt.show()
    # f/P
    freqTonov = []
    for index,size in enumerate(P):
        if index > len(P)/2:
            break
            
        if size > 200:
            print(index,size)
            freq = index * (fs/N)
            # freqTonov.append(index * (fs/N))
            # if len(freqTonov) >= 1:     
            #     if freqTonov[-1]-freq < 1:
            #         freq = (freqTonov[-1] + freq) / 2
            #         freqTonov.remove(freqTonov[-1])
            freqTonov.append(freq) 
                
    for freq in freqTonov:
        
    print(freqTonov)
        #MATPLOTLIB NI GOR PAZI ZA ODDAJANJE
    # for index,size in enumerate(f):
    #     if size > 2000:
    #         print(index, size)
            
    
    izhod = ''
    return izhod