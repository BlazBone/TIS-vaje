import numpy as np
from scipy.io.wavfile import write
from matplotlib import pyplot as plt

T = 2
fs = 44100
N = T * fs
print(f"vhod je dolg {T}")

# casovna os
t = np.arange(0,N,1) / fs
A_C1 = 1.0 # amplituda C1
A_E1 = 1.0 # amplituda C1
A_G1 = 1.0 # amplituda C1

f_C1 = 261.63 #ton C1
f_E1 = 329.63 #ton E1
f_G1 = 392.00 #ton G1
pit = 2*np.pi*t
x = A_C1 * np.sin(pit* f_C1 ) + A_E1 * np.sin(pit* f_E1 ) + A_G1 * np.sin(pit* f_G1 )
x= x/max(abs(x)) #normalizacija na interval od -1 do 1
print(x)
# zapisemo v datoteko
write("C_dur.wav", fs, x.astype(np.float32))

###################################3
# to so narediil profesorji zdj pa moramo mi to razresit
#razpoznamo akord

f = np.arange(0,N) * (fs/N) #frekvencna os
#DFT
X = np.fft.fft(x)

#mocnosti spekter
P = np.square( np.abs(X)) /N


figure, axis = plt.subplots(2,1)
axis[0].plot(t,x, color='blue')
axis[0].set_title("jakost v odvisnosti od casa")
axis[0].set_xlabel("t[s]")

axis[1].plot(f,P, color='red')
axis[1].set_title("moc v  odvisnosti od frekvence")
axis[1].set_xlabel("f[Hz]")
plt.show()
print(f)
# for item in f:
    # ce ne razpoznamo akorda vrnemo prazn niz..... akak ce dobimo naprimer 4 tone vrnemo nic ce dobimo 2 tona tudi... ce dobimo motilino frekvenco map jo samo ignoramo
#MATPLOTLIB NI GOR PAZI ZA ODDAJANJE
