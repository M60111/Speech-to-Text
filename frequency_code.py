# -*- coding: utf-8 -*-
"""Frequency Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12STA77HJVWEzWImt_8kQUoDrGS82kXCC
"""

import matplotlib.pyplot as plt

from scipy.io import wavfile

samplerate, data = wavfile.read("MTEST1.wav")

samplerate

data.shape

samples = data.shape[0]
samples

plt.plot(data[:1000000])

from scipy.fftpack import fft,fftfreq

datafft = fft(data)
fftabs = abs(datafft)

freqs = fftfreq(samples,1/samplerate)

plt.plot(freqs,fftabs)

plt.xlim( [10, samplerate/2] )
plt.xscale( 'log' )
plt.grid( True )
plt.xlabel( 'Frequency (Hz)' )
plt.plot(freqs[:int(freqs.size/2)],fftabs[:int(freqs.size/2)])

samplerate, data = wavfile.read("MTEST1.wav")
data.shape

samples = data.shape[0]
samples

plt.plot(data[:4*samplerate])

data = data[:,0]
data.shape

plt.plot(data[:4*samplerate])

datafft = fft(data)
fftabs = abs(datafft)
freqs = fftfreq(samples,1/samplerate)
plt.xlim( [10, samplerate/2] )
plt.xscale( 'log' )
plt.grid( True )
plt.xlabel( 'Frequency (Hz)' )
plt.plot(freqs[:int(freqs.size/2)],fftabs[:int(freqs.size/2)])
