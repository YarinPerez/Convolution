# 1D Signal Simulation and Convolution Analysis

This project is a Python application that demonstrates the use of 1D convolution to find a pattern within a simulated 1D signal. The program provides a visual representation of the signal, the selected pattern (kernel), the convolution result, and the matched patterns.

## Features

*   **Signal Generation:** Generates a 1D signal based on a sine function.
*   **Interactive Pattern Selection:** Allows the user to select a segment of the signal to be used as a pattern for matching.
*   **Convolution:** Performs normalized cross-correlation to find the occurrences of the selected pattern in the signal.
*   **Pattern Matching:** Identifies the locations where the pattern appears in the signal based on the convolution result.
*   **Visualization:** Displays the original signal, the selected pattern, the matched patterns, and the convolution result in separate plots.
*   **Image Output:** Saves the visualizations as `signal_and_matches.png` and `convolution_result.png`.

## How it Works

1.  The program starts and displays a plot of one cycle of the generated sine wave signal.
2.  The user selects a segment of the signal from the plot by clicking and dragging the mouse. This selected segment is used as the convolution kernel.
3.  The program automatically performs the convolution and identifies matching patterns.
4.  The program displays two separate plots:
    *   A plot showing the original signal, the selected segment, and the matching patterns.
    *   A separate plot showing the convolution result.
5.  The program saves the two plots as `signal_and_matches.png` and `convolution_result.png`.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/convolution-analysis.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd convolution-analysis
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: You may need to create a `requirements.txt` file first. See the dependencies section below.*

## Usage

To run the program, execute the following command in your terminal:

```bash
python main.py
```

## Dependencies

The program requires the following Python libraries:

*   `numpy`
*   `matplotlib`

You can install them using pip:

```bash
pip install numpy matplotlib
```

## Output

The program will generate and save two image files in the project's root directory:

*   `signal_and_matches.png`: A plot showing the original signal, the selected pattern (kernel), and the identified matching patterns.
*   `convolution_result.png`: A plot showing the result of the convolution operation.
