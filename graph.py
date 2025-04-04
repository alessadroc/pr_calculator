import tkinter as tk
from events import Events

class Graph:
    def __init__(self, root, event, placement):
        self.root = root
        self.event = event
        self.placement = placement

    def window(self):
        graph_window = tk.Toplevel(self.root)
        graph_window.title(f"Graph of {self.event} placement")