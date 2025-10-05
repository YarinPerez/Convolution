import numpy as np
from scipy.signal import find_peaks

def find_pattern_locations(correlation, threshold=0.8):
    """
    Finds the locations of a pattern in a signal based on the correlation result.

    Args:
        correlation (numpy.ndarray): The correlation result.
        threshold (float): The threshold for peak detection.

    Returns:
        numpy.ndarray: The indices of the matched patterns.
    """
    peaks, _ = find_peaks(correlation, height=threshold * np.max(correlation))
    return peaks
