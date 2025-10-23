# Implementation Tasks

## 1. Project Setup
- [ ] Choose and install necessary libraries for numerical computation (e.g., NumPy) and plotting (e.g., Matplotlib or Plotly).
- [ ] Configure uv Virtual Environment

## 2. Signal Generation
- [ ] Implement a function to generate the sine wave signal based on the specified parameters (10 cycles, 200 samples per cycle).
- [ ] Write unit tests to verify the correctness of the signal generation.

## 3. Input Handling
- [ ] Implement functionality to parse the start and end points (in radians) provided as command-line arguments to define the pattern segment.

## 4. Convolution
- [ ] Implement the convolution operation between the signal and the selected segment (kernel).
  > **Note:** The convolution should be implemented in a way that the result peaks when the pattern is matched. This can be achieved by using normalized cross-correlation or by manipulating the kernel.
- [ ] Write unit tests to verify the correctness of the convolution implementation.

## 5. Pattern Matching
- [ ] Implement the logic to identify the peaks in the convolution output, which correspond to the matched patterns.
- [ ] Implement a function to extract the indices of the matched patterns in the original signal.

## 6. Visualization
- [ ] Implement the visualization of the original signal, the selected pattern, and the highlighted matched patterns in a single plot.
- [ ] Implement the visualization of the convolution result in a separate plot.

## 7. Output
- [ ] Implement Image Save: Add a feature to save the visualizations as an image file (e.g., PNG).
- [ ] Print Convolution Result to Console: Implement functionality to print the convolution result to the console.

## 8. Main Application
- [ ] Integrate all the components into a single application.
- [ ] Implement the main user flow: generate signal, parse pattern argument, perform convolution, save images, and print result to console.

## 9. Documentation and Refinements
- [ ] Add comments and documentation to the code.
- [ ] Refine the visualizations for clarity and ease of use.
- [ ] Create a `README.md` file with instructions on how to run the program.