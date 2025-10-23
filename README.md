# 1D Signal Simulation and Convolution Analysis

This project is a Python application that demonstrates the use of 1D convolution to find a pattern within a simulated 1D signal. The program provides a visual representation of the signal, the selected pattern (kernel), the convolution result, and the matched patterns.

## Features

*   **Signal Generation:** Generates a 1D signal based on a sine function.
*   **Pattern Selection:** Allows the user to provide a segment of the signal as a command-line argument to be used as a pattern for matching.
*   **Convolution:** Performs normalized cross-correlation to find the occurrences of the selected pattern in the signal.
*   **Pattern Matching:** Identifies the locations where the pattern appears in the signal based on the convolution result.
*   **Visualization:** Displays the original signal, the selected pattern, the matched patterns, and the convolution result in separate plots.
*   **Image Output:** Saves the visualizations as `signal_and_matches.png` and `convolution_result.png`.

## How it Works

1.  The program starts, taking a segment of the generated sine wave signal as a command-line argument to be used as the convolution kernel.
2.  The program automatically performs the convolution and identifies matching patterns.
3.  The program displays two separate plots:
    *   A plot showing the original signal, the selected segment, and the matching patterns.
    *   A separate plot showing the convolution result.
4.  The program saves the two plots as `signal_and_matches.png` and `convolution_result.png`.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/convolution-analysis.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd convolution-analysis
    ```
3.  Create a virtual environment using `uv`:
    ```bash
    uv venv
    ```
4.  Activate the virtual environment:
    - On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source .venv/bin/activate
        ```
5.  Install the required dependencies:
    ```bash
    uv pip install -r requirements.txt
    ```

## Usage

To run the program, execute the following command in your terminal, providing the start and end points (in radians) of the pattern within a single sine wave cycle:

```bash
python main.py --start_point 0.0 --end_point 1.57
```

## Dependencies

The program requires the following Python libraries:

*   `numpy`
*   `matplotlib`

To generate a `requirements.txt` file, you can use:

```bash
python -m pip freeze > requirements.txt
```

Then, install them using `uv`:

```bash
uv pip install -r requirements.txt
```

## Output

The program will generate and save two image files in the project's root directory:

*   `signal_and_matches.png`: A plot showing the original signal, the selected pattern (kernel), and the identified matching patterns.
*   `convolution_result.png`: A plot showing the result of the convolution operation.
