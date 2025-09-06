import numpy as np
import matplotlib.pyplot as plt

def sine_wave(A, f, phi, t):
    """
    Generate and plot a sine wave: s(t) = A * sin(2*pi*f*t + phi)
    A: amplitude, f: frequency (Hz), phi: phase (rad), t: time vector (NumPy array)
    Returns: NumPy array of sine signal
    """
    sine = A * np.sin(2 * np.pi * f * t + phi)
    plt.figure()
    plt.plot(t, sine)
    plt.title("Sine Wave")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return sine

def cosine_wave(A, f, phi, t):
    """
    Generate and plot a cosine wave: c(t) = A * cos(2*pi*f*t + phi)
    Returns: NumPy array of cosine signal
    """
    cosine = A * np.cos(2 * np.pi * f * t + phi)
    plt.figure()
    plt.plot(t, cosine)
    plt.title("Cosine Wave")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return cosine

def exponential_signal(A, a, t):
    """
    Generate and plot an exponential signal: e(t) = A * exp(a*t)
    Returns: NumPy array of exponential signal
    """
    expo = A * np.exp(a * t)
    plt.figure()
    plt.plot(t, expo)
    plt.title("Exponential Signal")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return expo
