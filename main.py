import numpy as np

import numpy as np
from signal_ICT_RudraMiyani_92400133129.unitary_signals import unit_step, unit_impulse, ramp_signal
from signal_ICT_RudraMiyani_92400133129.trigonometric_signals import sine_wave, cosine_wave
from signal_ICT_RudraMiyani_92400133129.operations import time_shift, signal_addition, signal_multiplication

# Rest of your code remains the same

# 1. Generate and plot unit step and unit impulse signals of length 20
n = np.arange(0, 20)
step = unit_step(n)
impulse = unit_impulse(n)

# 2. Generate a sine wave (A=2, f=5 Hz, phi=0, t=0..1 s)
t = np.linspace(0, 1, 500)
sine = sine_wave(2, 5, 0, t)

# 3. Time shifting: shift sine wave by +5 units (consider discrete points)
shift_amount = 5
sine_shifted = time_shift(sine, shift_amount)
import matplotlib.pyplot as plt
plt.figure()
plt.plot(t, sine, label='Original Sine')
plt.plot(t, sine_shifted, label='Shifted Sine (+5)')
plt.title("Sine Wave - Original vs Shifted")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# 4. Addition of unit step and ramp signal
ramp = ramp_signal(n)
added_signal = signal_addition(step, ramp)
plt.figure()
plt.stem(n, added_signal)
plt.title("Addition: Unit Step + Ramp Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# 5. Multiplication of sine and cosine waves (same frequency)
cosine = cosine_wave(2, 5, 0, t)
multiplied_signal = signal_multiplication(sine, cosine)
plt.figure()
plt.plot(t, multiplied_signal)
plt.title("Multiplication: Sine * Cosine Waves")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
