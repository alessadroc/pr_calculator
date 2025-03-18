from tkinter import *
from tkinter import ttk
from pr_calculation_model import calculate_pr

# Root window
root = Tk()
root.title("Fortnite Power Ranking Calculator")

# Variables
event = StringVar()
placement = StringVar()
output_var = StringVar(value="0") 

# Calculation Model Caller
def on_calculate():
    event_value = event.get()
    place_value = placement.get()
    result = calculate_pr(event_value, place_value)
    output_var.set(result)

# Frame
frm = ttk.Frame(root, padding=10)
frm.grid()

# Labels
dropdown_lbl = ttk.Label(frm, text="Event:", anchor="w")
dropdown_lbl.grid(column=0, row=1, sticky="w")

entry_label = ttk.Label(frm, text="Rank for this event:", anchor="w")
entry_label.grid(column=0, row=2, sticky="w")

# Dropdown
combo = ttk.Combobox(
    frm,
    state="readonly",
    values=["Solo Cash Cup Opens", "Solo Cash Cup Finals", "FNCS Division 1", "FNCS Division 2", "FNCS Division 3", "Performance Evaluation"],
    width=30,
    textvariable=event
)
combo.grid(column=1, row=1, sticky="w")

# Placement Entry
entry = ttk.Entry(frm, width=30, textvariable=placement)
entry.grid(column=1, row=2, sticky="w")

# Calculate Button
button = ttk.Button(frm, text="Calculate", width=30, command=on_calculate)
button.grid(column=1, row=3, sticky="w")

# Output Labels
output_text_lbl = ttk.Label(frm, text="PR Gained from this event:", anchor="w")
output_text_lbl.grid(column=0, row=4, sticky="w")

output_lbl = ttk.Label(frm, textvariable=output_var, anchor="w")
output_lbl.grid(column=1, row=4, sticky="w")

# Run the application
root.mainloop()
