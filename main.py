from src.signal_generator import generate_sine_wave
from src.convolution import normalized_cross_correlation
from src.pattern_matching import find_pattern_locations
from src.visualization import plot_results, plot_convolution, show_plots
import argparse
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="1D Signal Simulation and Convolution Analysis")
    parser.add_argument("--start_point", type=float, required=True,
                        help="Start point (in radians) of the pattern within a single sine wave cycle (0 to 2*pi).")
    parser.add_argument("--end_point", type=float, required=True,
                        help="End point (in radians) of the pattern within a single sine wave cycle (0 to 2*pi).")
    args = parser.parse_args()

    # Generate the signal
    x, signal = generate_sine_wave()

    # Validate input points
    if not (0 <= args.start_point < args.end_point <= 2 * np.pi):
        print("Error: start_point and end_point must be within 0 and 2*pi, and start_point must be less than end_point.")
        return

    # Find the indices corresponding to the start and end points within the first cycle
    # Assuming x is generated from 0 to 10 * 2 * pi, and we want to select from the first cycle.
    # The signal_generator generates 200 samples per cycle.
    samples_per_cycle = 200
    total_samples = len(x)
    samples_in_first_cycle = x[:samples_per_cycle]

    start_index_in_cycle = np.argmin(np.abs(samples_in_first_cycle - args.start_point))
    end_index_in_cycle = np.argmin(np.abs(samples_in_first_cycle - args.end_point))

    # Extract the kernel from the first cycle of the signal
    kernel = signal[start_index_in_cycle:end_index_in_cycle]
    kernel_x = x[start_index_in_cycle:end_index_in_cycle]

    if len(kernel) == 0:
        print("Error: Selected pattern is empty. Adjust start_point and end_point.")
        return

    # Perform convolution
    correlation = normalized_cross_correlation(signal, kernel)

    # Find matched patterns
    matches = find_pattern_locations(correlation)

    # Visualize the results
    plot_results(x, signal, kernel_x, kernel, matches)
    plot_convolution(x, correlation)

    # Print convolution result to console
    print("Convolution Result:")
    print(correlation)

    # Show the plots
    # show_plots()

if __name__ == "__main__":
    main()
