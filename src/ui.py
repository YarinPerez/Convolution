import matplotlib.pyplot as plt
import numpy as np

class SignalSelector:
    def __init__(self, x, signal):
        self.x = x
        self.signal = signal
        self.start_index = -1
        self.end_index = -1
        self.fig, self.ax = plt.subplots(figsize=(15, 5))
        
        # Show only one cycle for selection
        one_cycle_x = self.x[:200]
        one_cycle_y = self.signal[:200]
        self.ax.plot(one_cycle_x, one_cycle_y)
        
        self.ax.set_title('Click to select a segment of the signal from one cycle')
        self.ax.set_xlabel('Angle (radians)')
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        print("Please click on the plot to select the start and end of the segment.")
        plt.show()

    def on_press(self, event):
        if event.inaxes != self.ax:
            return
        
        # Find the index of the closest x value
        index = np.argmin(np.abs(self.x - event.xdata))
        
        if self.start_index == -1:
            self.start_index = index
            self.ax.axvline(self.x[self.start_index], color='r', linestyle='--')
            self.fig.canvas.draw()
            print(f"Start index selected: {self.start_index}")
        elif self.end_index == -1:
            self.end_index = index
            self.ax.axvline(self.x[self.end_index], color='r', linestyle='--')
            self.fig.canvas.draw()
            print(f"End index selected: {self.end_index}")
            plt.close(self.fig)

    def get_selected_indices(self):
        if self.start_index != -1 and self.end_index != -1:
            start = min(self.start_index, self.end_index)
            end = max(self.start_index, self.end_index)
            return start, end
        return None, None
