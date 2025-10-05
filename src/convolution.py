import numpy as np

def normalized_cross_correlation(signal, kernel):
    """
    Computes the normalized cross-correlation between a signal and a kernel.

    Args:
        signal (numpy.ndarray): The input signal.
        kernel (numpy.ndarray): The kernel (pattern) to search for.

    Returns:
        numpy.ndarray: The normalized cross-correlation result.
    """
    # Normalize the kernel
    kernel = (kernel - np.mean(kernel)) / np.std(kernel)
    
    # Pad the signal to handle borders
    padded_signal = np.pad(signal, (len(kernel) // 2, len(kernel) // 2), 'constant')
    
    correlation = np.zeros(len(signal))
    for i in range(len(signal)):
        segment = padded_signal[i:i + len(kernel)]
        # Normalize the segment
        if np.std(segment) > 0:
            segment = (segment - np.mean(segment)) / np.std(segment)
        correlation[i] = np.dot(segment, kernel)
        
    return correlation
