import matplotlib.pyplot as plt
import numpy as np

def plot_results(x, signal, kernel_x, kernel, matches):
    """
    Plots the signal, the kernel, and the matched patterns and saves it to a file.
    """
    plt.figure(figsize=(15, 5))
    plt.plot(x, signal, label='Signal')
    plt.plot(kernel_x, kernel, label='Pattern', linewidth=3)
    
    for i, match in enumerate(matches):
        start = match - len(kernel) // 2
        end = start + len(kernel)
        if start < 0 or end > len(signal):
            continue
        
        matched_segment = signal[start:end]
        matched_x = x[start:end]
        
        if i == 0:
            plt.plot(matched_x, matched_segment, 'r--', linewidth=2, label='Matched Pattern')
        else:
            plt.plot(matched_x, matched_segment, 'r--', linewidth=2)
        
    plt.legend()
    plt.title('Signal with Matched Patterns')
    plt.xlabel('Angle (radians)')
    plt.savefig("signal_and_matches.png")

def plot_convolution(x, correlation):
    """
    Plots the convolution result and saves it to a file.
    """
    plt.figure(figsize=(15, 5))
    plt.plot(x, correlation, label='Convolution Result')
    plt.legend()
    plt.title('Convolution Result')
    plt.xlabel('Angle (radians)')
    plt.savefig("convolution_result.png")

def show_plots():
    """
    Shows all the plots.
    """
    plt.show()
