# Product Requirements Document: 1D Signal Simulation and Convolution Analysis

## 1. Introduction/Background

This document outlines the requirements for a program that simulates a 1D signal as a sine function, applies a convolution operation to find a pattern within the signal, and provides detailed visualizations of the entire process.

## 2. Problem Statement

The program aims to provide a clear and detailed visual representation of how convolution can be used to detect patterns in a 1D signal. This will be useful for educational and analytical purposes.

## 3. Goals/Objectives

*   To provide an interactive and visual tool for learning about 1D convolution.
*   To clearly demonstrate the relationship between a signal, a kernel, and the resulting convolved signal.
*   To allow users to experiment with different signals and kernels to understand their impact on the convolution output.

## 4. Target Audience

This program is intended for general educational purposes and is not tailored to a specific audience.

## 5. Features and Functionality

*   **Signal Generation:** The program will generate a 1D signal based on a sine function. The parameters of the sine wave (frequency, amplitude, phase) will be fixed.
*   **Pattern Selection:** The user will be able to select a segment of the generated signal by clicking on a plot showing one cycle of the sine wave. This selected segment will be used as the pattern to search for in the signal.
*   **Convolution:** The program will perform a normalized cross-correlation between the entire signal and the selected pattern (kernel) to ensure the result peaks when the pattern is matched.
*   **Pattern Matching:** The output of the convolution will be used to identify all the locations where the pattern appears in the signal by finding the peaks in the correlation result.
*   **Visualization:**
    *   The original signal, the selected pattern (kernel), and the identified matching patterns will be displayed together in one plot. The x-axis of the plot will represent the angle of the sine wave in radians.
    *   The result of the convolution operation will be displayed in a separate plot, with the x-axis representing the angle in radians.
*   **Image Output:** The program will generate and save two separate image files: `signal_and_matches.png` and `convolution_result.png`.

## 6. User Flow

1.  The program starts and displays a plot of one cycle of the generated sine wave signal.
2.  The user selects a segment of the signal from the plot to be used as the convolution kernel.
3.  The program automatically performs the convolution and identifies matching patterns.
4.  The program displays the visualizations in separate windows:
    *   A plot showing the original signal, the selected segment, and the matching patterns.
    *   A separate plot showing the convolution result.
5.  The program saves the two plots as `signal_and_matches.png` and `convolution_result.png`.

## 7. Non-Functional Requirements

*   **Signal Generation:**
    *   The sine wave signal will consist of 10 cycles (10 * 2pi).
    *   Each cycle will be sampled 200 times, resulting in a total of 2000 samples for the entire signal.
*   **Usability:**
    *   The user's selection of a signal segment should be aligned with the discrete sample points of the signal. This ensures that the selected pattern can be perfectly matched and highlighted in the signal.
*   **Dependencies:**
    *   The program will use `numpy` for numerical computation and `matplotlib` for plotting.

## 8. Success Metrics

*   **Clarity of Visualization:** The visualizations of the signal, kernel, convolution result, and matched patterns are clear and easy to interpret.
*   **Correctness of Results:** The program accurately identifies all occurrences of the selected pattern in the signal.