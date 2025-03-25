import tkinter as tk
from tkinter import ttk
from pr_calculation_model import calculate_pr
from PIL import Image, ImageTk

# Root window
root = tk.Tk()
root.title("Fortnite Power Ranking Calculator")

# Power Ranking icon
icon = Image.open('pr_icon.png')
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False, photo)

# Variables
event = tk.StringVar()
placement = tk.StringVar(root)
output_var = tk.StringVar(value="0") 

# Calculation Model Caller
def on_calculate():
    event_value = event.get()
    place_value = placement.get()
    result = calculate_pr(event_value, place_value)
    output_var.set(result)

# Frame
frm = tk.Frame(root, padx=5, pady=5)
frm.grid()

# Labels
dropdown_lbl = tk.Label(frm, text="Event:", anchor="w", pady=5)
dropdown_lbl.grid(column=0, row=1, sticky="w")

entry_label = tk.Label(frm, text="Rank for this event:", anchor="w", pady=5)
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
entry = tk.Entry(frm, width=30, textvariable=placement, relief="flat")
entry.grid(column=1, row=2, sticky="w")

# Calculate Button
button = tk.Button(frm, text="Calculate", width=30, bg="purple", fg="white", command=on_calculate, relief="flat")
button.grid(column=1, row=3, sticky="w")

# Output Labels
output_text_lbl = tk.Label(frm, text="PR Gained", anchor="w", pady=5)
output_text_lbl.grid(column=0, row=4, sticky="w")

output_lbl = tk.Label(frm, font=("System", 15), fg="purple", textvariable=output_var, anchor="w")
output_lbl.grid(column=1, row=4, sticky="w")

# Run the application
root.mainloop()
