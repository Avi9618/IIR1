import numpy as np
import scipy.signal as sc
import matplotlib.pyplot as plt

Ap=0.6
As=0.1
T=0.1
Os=0.7
Op=0.35
N=0.5*np.log(((1/As**2)-1)/((1/Ap**2)-1))/np.log(Os/Op)
N=np.round(N)

Oc=Os/(np.power(((1/0.1**2)-1),(1/2*N)))
wc=2*np.tan(Oc*T/2)

def butter_lowpass(wc, fs, N):
    nyq = 0.5 * fs
    normal_wc = wc / nyq
    b, a = sc.butter(N, normal_wc, btype='low', analog=False)
    return b, a

fs =1/T
b, a = butter_lowpass(wc, fs, N)

w, h = sc.freqz(b, a)
plt.subplot(2, 1, 1)
plt.plot(w, np.abs(h), 'b')
plt.subplot(2, 1, 2)
plt.plot(w, 10*np.log(np.abs(h)/np.abs(max(h))), 'b')
