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


    figure, axis = plt.subplots(2,1)
    # axis[0].plot(t,x, color='blue')
    # axis[0].set_title("jakost v odvisnosti od casa")
    # axis[0].set_xlabel("t[s]")

    axis[1].plot(f,P, color='red')
    axis[1].set_title("moc v  odvisnosti od frekvence")
    axis[1].set_xlabel("f[Hz]")
    plt.show()
        #MATPLOTLIB NI GOR PAZI ZA ODDAJANJE
    
    izhod = ''
    return izhod