import numpy as np
import matplotlib.pyplot as plt 

#Setting up example waves
time_period = 3.0
example_ratePerSec = 1000
frequency = 4.0 

t = np.linspace(0, time_period, int(example_ratePerSec * time_period))

sin_waveA = np.sin(2*np.pi*frequency*t)
square_waveA = np.sign(sin_waveA)
converted_waveA = (square_waveA + 1)/2

phase_shift = np.pi / 2

sin_waveB = np.sin(2*np.pi*frequency*t + phase_shift)
square_waveB = np.sign(sin_waveB)
converted_waveB = (square_waveB + 1)/2
