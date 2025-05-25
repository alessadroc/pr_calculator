import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pr_calculation_model import calculate_pr
from graph import Graph

# Fundamentals
root = tk.Tk()
root.title("Fortnite Power Ranking Calculator")

icon = Image.open('pr_icon.png')
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False, photo)

event = tk.StringVar()
placement = tk.StringVar(root)
output_var = tk.StringVar(value="0")

# Do this when Graph is clicked
def graph_result():
    # problematic code; logic is correct but doesn't reset after the user hits the graph btn after invalid input
    '''
    try:
        inted_place = int(event.get())
        if not 0 < inted_place <= 10000:
            result_graph = Graph(root, event.get(), placement.get())
            result_graph.window()
    except ValueError:
      exception_window = tk.Tk()
      exception_window.title("Error")

      exception_lbl = tk.Label(exception_window, text="Cannot create graph for this value.", pady=50, padx=50)  
      exception_lbl.pack()
    '''
    result_graph = Graph(root, event.get(), placement.get())
    result_graph.window()

# Do this when calculate is clicked
def on_calculate():

    result = None
    event_value = event.get()
    place_value = placement.get()

    result = calculate_pr(event_value, place_value)
    output_var.set(result)
    
    graph_btn = tk.Button(frm, text="Graph", width=30, bg="purple", fg="white", command=graph_result, relief="flat")
    
    if result is not None:
        graph_btn.grid(column=1, row=5, sticky='w')
    else:
        graph_btn.destroy()

# Frame
frm = tk.Frame(root, padx=5, pady=5)
frm.grid()

# Labels
dropdown_lbl = tk.Label(frm, text="Event:", anchor="w", pady=5)
dropdown_lbl.grid(column=0, row=1, sticky="w")

entry_label = tk.Label(frm, text="Rank for this event: #", anchor="w", pady=5)
entry_label.grid(column=0, row=2, sticky="w")

# Dropdown
combo = ttk.Combobox(
    frm,
    state="readonly",
    values=["Solo Cash Cup Opens", "Solo Cash Cup Finals", "FNCS Division 1", "FNCS Division 2", "FNCS Division 3", "Performance Evaluation Opens", "Performance Evaluation Finals"],
    width=30,
    textvariable=event
)
combo.grid(column=1, row=1, sticky="w")

# Placement Entry
entry = tk.Entry(frm, width=30, textvariable=placement, relief="flat", border=3)
entry.grid(column=1, row=2, sticky="w")

# Calculate Button
button = tk.Button(frm, text="Calculate", width=30, bg="purple", fg="white", command=on_calculate, relief="flat")
button.grid(column=1, row=3, sticky="w")

# Output Labels
output_text_lbl = tk.Label(frm, text="PR Gained", anchor="w", pady=5)
output_text_lbl.grid(column=0, row=4, sticky="w")

output_lbl = tk.Label(frm, font=("System", 15), fg="purple", textvariable=output_var, anchor="w", pady=10)
output_lbl.grid(column=1, row=4, sticky="w")

# Run the application
root.mainloop()