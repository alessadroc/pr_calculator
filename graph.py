import tkinter as tk

class Graph:
    def __init__(self, root, event):
        self.root = root
        self.event = event

    def window(self):
        graph_window = tk.Toplevel(self.root)
        graph_window.title(f"Graph of {self.event} placement")

        window_frm = tk.Frame(graph_window)
        window_frm.grid()

        test_lbl = tk.Label(window_frm, text="Test Label")
        test_lbl.grid(row=0,column=0)