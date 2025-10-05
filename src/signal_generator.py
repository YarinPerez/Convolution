import numpy as np

def generate_sine_wave(cycles=10, samples_per_cycle=200):
    """
    Generates a sine wave signal.

    Args:
        cycles (int): The number of cycles in the sine wave.
        samples_per_cycle (int): The number of samples per cycle.

    Returns:
        tuple: A tuple containing the x and y values of the sine wave.
    """
    total_samples = cycles * samples_per_cycle
    x = np.linspace(0, cycles * 2 * np.pi, total_samples)
    y = np.sin(x)
    return x, y