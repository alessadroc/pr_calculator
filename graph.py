import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from events import Events

class Graph:
    def __init__(self, root, event, placement):
        self.root = root
        self.event = event
        self.placement = placement

    def window(self):
        graph_window = tk.Toplevel(self.root)
        graph_window.title(f"Graph of {self.event} placement")

        fig = self.plot_graph()

        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def plot_graph(self):
        data = self.lobf(self.event)

        x, y = zip(*data)
        x = np.array(x)
        y = np.array(y)

        # Get line of best fit
        m, b = np.polyfit(x, y, 1)
        lobf_y = m * x + b

        # Matplotlib figure
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        ax.scatter(x, y, color='purple', label='Data Points')
        ax.plot(x, lobf_y, color='black', linestyle='--', label='Line of Best Fit')

        ax.set_title(f"{self.event} Placement vs Points")
        ax.set_xlabel("Placement")
        ax.set_ylabel("Points")
        ax.legend()

        return fig

    def lobf(self, event):
        events = Events()
        try:
            event_method_name = event.lower().replace(" ", "_")
            func = getattr(events, event_method_name)
        except AttributeError:
            print(f"Event '{event}' not found in Events.")
            return []

        ranges_dict = func()
        xy = []

        for placement_range, points in ranges_dict.items():
            start, end = placement_range
            for placement in range(start, end + 1):
                xy.append((placement, points))

        return xy
