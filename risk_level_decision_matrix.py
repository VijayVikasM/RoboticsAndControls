import tkinter as tk
from tkinter import ttk

# RLDM logic
def calculate_risk():
    severity = severity_var.get()
    exposure = exposure_var.get()
    avoidance = avoidance_var.get()

    risk = "Unknown"  # Default

    if severity == "S1 (Minor)":
        if exposure == "E0 (Prevented)":
            risk = "Negligible"
        elif exposure == "E1 (Low)":
            risk = "Low" if avoidance in ["A2 (Not Likely)", "A3 (Not Possible)"] else "Negligible"
        elif exposure == "E2 (High)":
            risk = "Low"
    elif severity == "S2 (Moderate)":
        if exposure == "E0 (Prevented)":
            risk = "Low"
        elif exposure == "E1 (Low)":
            risk = "Medium"
        elif exposure == "E2 (High)":
            risk = "High" if avoidance in ["A2 (Not Likely)", "A3 (Not Possible)"] else "Medium"
    elif severity == "S3 (Serious)":
        if exposure == "E0 (Prevented)":
            risk = "Low"
        elif exposure == "E1 (Low)":
            risk = "High"
        elif exposure == "E2 (High)":
            risk = "High" if avoidance in ["A2 (Not Likely)", "A1 (Likely)"] else "Very High"

    result_label.config(text=f"Risk Level: {risk}", foreground="red" if risk in ["High", "Very High"] else "green")

# Main application window
root = tk.Tk()
root.title("Risk Level Decision Matrix")
root.geometry("400x300")

# Define input variables
severity_var = tk.StringVar()
exposure_var = tk.StringVar()
avoidance_var = tk.StringVar()

# GUI Elements
ttk.Label(root, text="Severity of Injury:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
severity_menu = ttk.Combobox(root, textvariable=severity_var, state="readonly", width=25)
severity_menu["values"] = ["S1 (Minor)", "S2 (Moderate)", "S3 (Serious)"]
severity_menu.grid(row=0, column=1, padx=10, pady=10)
severity_menu.current(0)

ttk.Label(root, text="Exposure to the Hazard:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
exposure_menu = ttk.Combobox(root, textvariable=exposure_var, state="readonly", width=25)
exposure_menu["values"] = ["E0 (Prevented)", "E1 (Low)", "E2 (High)"]
exposure_menu.grid(row=1, column=1, padx=10, pady=10)
exposure_menu.current(0)

ttk.Label(root, text="Avoidance of the Hazard:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
avoidance_menu = ttk.Combobox(root, textvariable=avoidance_var, state="readonly", width=25)
avoidance_menu["values"] = ["A1 (Likely)", "A2 (Not Likely)", "A3 (Not Possible)"]
avoidance_menu.grid(row=2, column=1, padx=10, pady=10)
avoidance_menu.current(0)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate Risk", command=calculate_risk)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Result label
result_label = ttk.Label(root, text="Risk Level: ", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run application
root.mainloop()
