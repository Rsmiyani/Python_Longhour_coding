import numpy as np

def time_shift(signal, k):
    """
    Shift a signal by k units.
    Positive k = right shift; negative k = left shift.
    Returns: shifted signal (NumPy array)
    """
    shifted = np.roll(signal, k)
    return shifted

def time_scale(signal, k):
    """
    Scale the time axis of the signal by factor k (downsampling if k > 1).
    Returns: downsampled signal (NumPy array)
    """
    scaled = signal[::k]
    return scaled

def signal_addition(signal1, signal2):
    """
    Add two signals element-wise. Signals must be same length.
    Returns: sum signal (NumPy array)
    """
    added = signal1 + signal2
    return added

def signal_multiplication(signal1, signal2):
    """
    Multiply two signals element-wise. Signals must be same length.
    Returns: product signal (NumPy array)
    """
    multiplied = signal1 * signal2
    return multiplied
