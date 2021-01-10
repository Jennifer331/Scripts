import numpy as np
import matplotlib.pyplot as plt

samplingFrequency = 100

samplingInterval = 1/samplingFrequency

beginTime = 0
endTime = 10

f1 = 4
f2 = 7

time = np.arange(beginTime, endTime, samplingInterval)

data1 = np.cos(2*np.pi*f1*time)
data2 = np.cos(2*np.pi*f2*time)

figure, axis = plt.subplots(4, 1)

axis[0].plot(time, data1)
axis[1].plot(time, data2)
data = data1 + data2
axis[2].plot(time, data)

fft = np.fft.fft(data)/len(data)
fft = fft[range(int(len(data)/2))]

tpCount = len(data)
values = np.arange(int(tpCount/2))
timePeroid = tpCount/samplingFrequency
frequencies = values/timePeroid

axis[3].plot(frequencies, abs(fft))

plt.show()

def drawfft(data, axis):
    fft = np.fft.fft(data) / len(data)
    fft = fft[range(int(len(data) / 2))]

    tpCount = len(data)
    values = np.arange(int(tpCount / 2))
    timePeroid = tpCount / samplingFrequency
    frequencies = values / timePeroid

    axis[3].plot(frequencies, abs(fft))