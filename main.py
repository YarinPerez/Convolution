from src.signal_generator import generate_sine_wave
from src.ui import SignalSelector
from src.convolution import normalized_cross_correlation
from src.pattern_matching import find_pattern_locations
from src.visualization import plot_results, plot_convolution, show_plots

def main():
    # Generate the signal
    x, signal = generate_sine_wave()

    # Let the user select a segment
    selector = SignalSelector(x, signal)
    start_index, end_index = selector.get_selected_indices()
    
    if start_index is not None and end_index is not None:
        kernel = signal[start_index:end_index]
        kernel_x = x[start_index:end_index]

        if len(kernel) > 0:
            # Perform convolution
            correlation = normalized_cross_correlation(signal, kernel)

            # Find matched patterns
            matches = find_pattern_locations(correlation)

            # Visualize the results
            plot_results(x, signal, kernel_x, kernel, matches)
            plot_convolution(x, correlation)

            # Show the plots
            show_plots()
    else:
        print("No segment selected or segment is empty.")

if __name__ == "__main__":
    main()
