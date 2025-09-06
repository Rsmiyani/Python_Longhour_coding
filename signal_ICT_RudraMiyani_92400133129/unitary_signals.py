import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    """
    Generate and plot a unit step signal (u[n]).
    Returns: NumPy array representing the signal.
    """
    step = np.where(n >= 0, 1, 0)
    plt.figure()
    plt.stem(n, step)
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return step

def unit_impulse(n):
    """
    Generate and plot a unit impulse signal (delta[n]).
    Returns: NumPy array representing the signal.
    """
    impulse = np.where(n == 0, 1, 0)
    plt.figure()
    plt.stem(n, impulse)
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return impulse

def ramp_signal(n):
    """
    Generate and plot a ramp signal (r[n] = n for n >= 0, else 0).
    Returns: NumPy array representing the signal.
    """
    ramp = np.where(n >= 0, n, 0)
    plt.figure()
    plt.stem(n, ramp)
    plt.title("Ramp Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return ramp
