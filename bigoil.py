import tkinter as tk
from tkinter import ttk

# Exact reactor data with fixed properties
reactors = {
    1: {"color": "Yellow", "valves": "1 valve", "pressure": "<", "element": "Nitrogen", "room": "Right", "row": "Row 1"},
    2: {"color": "Blue", "valves": "1 valve", "pressure": ">", "element": "Deuterium", "room": "Right", "row": "Row 1"},
    3: {"color": "Green", "valves": "1 valve", "pressure": "=", "element": "Helium", "room": "Left", "row": "Row 2"},
    4: {"color": "Yellow", "valves": "2 valves", "pressure": "=", "element": "Nitrogen", "room": "Left", "row": "Row 2"},
    5: {"color": "Blue", "valves": "2 valves", "pressure": "<", "element": "Deuterium", "room": "Left", "row": "Row 3"},
    6: {"color": "Green", "valves": "2 valves", "pressure": ">", "element": "Helium", "room": "Left", "row": "Row 3"},
    7: {"color": "Green", "valves": "3 valves", "pressure": "<", "element": "Helium", "room": "Left", "row": "Row 1"},
    8: {"color": "Yellow", "valves": "3 valves", "pressure": "<", "element": "Nitrogen", "room": "Left", "row": "Row 3"},
    9: {"color": "Blue", "valves": "3 valves", "pressure": "<", "element": "Deuterium", "room": "Right", "row": "Row 2"},
    10: {"color": "Green", "valves": "3 valves", "pressure": "=", "element": "Helium", "room": "Right", "row": "Row 2"},
    11: {"color": "Yellow", "valves": "3 valves", "pressure": ">", "element": "Nitrogen", "room": "Right", "row": "Row 3"},
    12: {"color": "Blue", "valves": "3 valves", "pressure": ">", "element": "Deuterium", "room": "Right", "row": "Row 3"}
}

def find_reactor():
    """Main function to find the correct reactor"""
    # Get values from dropdown menus
    selected_color = color_var.get()
    selected_valves = valves_var.get()
    selected_pressure = pressure_var.get()
    
    # Extract just the color part from selection (remove element in parentheses)
    selected_color_only = selected_color.split(" (")[0] if " (" in selected_color else selected_color
    
    # Validation
    if not selected_color_only or not selected_valves or not selected_pressure:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please fill all fields!")
        return
    
    # Convert pressure selection to symbol
    pressure_symbol = ">" if selected_pressure == "≥5783 psi" else "<" if selected_pressure == "≤5812 psi" else "="
    
    # Find matching reactors
    matching_reactors = []
    for reactor_num, props in reactors.items():
        if (props["color"] == selected_color_only and 
            props["valves"] == selected_valves and 
            props["pressure"] == pressure_symbol):
            matching_reactors.append((reactor_num, props))
    
    # Display results
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Search: {selected_color}, {selected_valves}, {selected_pressure}\n")
    result_text.insert(tk.END, "=" * 60 + "\n\n")
    
    if matching_reactors:
        result_text.insert(tk.END, f"Found {len(matching_reactors)} matching reactor(s):\n\n")
        
        for reactor_num, props in matching_reactors:
            pressure_desc = "≥5783 psi (>400 bar)" if props["pressure"] == ">" else "≤5812 psi (<400 bar)" if props["pressure"] == "<" else "=400 bar"
            
            result_text.insert(tk.END, f"REACTOR #{reactor_num}\n")
            result_text.insert(tk.END, f"Location: {props['room']} Room, {props['row']}\n")
            result_text.insert(tk.END, f"Element: {props['element']}\n")
            result_text.insert(tk.END, f"Color: {props['color']}\n")
            result_text.insert(tk.END, f"Valves: {props['valves']}\n")
            result_text.insert(tk.END, f"Pressure: {pressure_desc}\n")
            result_text.insert(tk.END, "-" * 40 + "\n")
    else:
        result_text.insert(tk.END, "No reactors found matching all criteria!\n\n")
        result_text.insert(tk.END, "Note: Reactors 3, 4, and 10 always have =400 bar pressure\n")
        result_text.insert(tk.END, "and will NEVER be the correct choice in any game session.\n\n")
        
        # Show what reactors exist with these color/valves
        similar_reactors = []
        for reactor_num, props in reactors.items():
            if (props["color"] == selected_color_only and 
                props["valves"] == selected_valves):
                similar_reactors.append((reactor_num, props))
        
        if similar_reactors:
            result_text.insert(tk.END, f"Reactors with {selected_color}, {selected_valves}:\n")
            for reactor_num, props in similar_reactors:
                pressure_desc = "≥5783 psi" if props["pressure"] == ">" else "≤5812 psi" if props["pressure"] == "<" else "=400 bar"
                result_text.insert(tk.END, f"  #{reactor_num}: {pressure_desc} ({props['element']})\n")

def show_all_reactors():
    """Show all reactors for reference"""
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "ALL REACTORS - Reference Table\n")
    result_text.insert(tk.END, "=" * 60 + "\n\n")
    
    result_text.insert(tk.END, "LEFT ROOM:\n")
    result_text.insert(tk.END, "Row 1: #12(Blue/Deuterium,3,>)  #7(Green/Helium,3,<)\n")
    result_text.insert(tk.END, "Row 2: #10(Green/Helium,3,=)  #9(Blue/Deuterium,3,<)\n") 
    result_text.insert(tk.END, "Row 3: #8(Yellow/Nitrogen,3,<)  #11(Yellow/Nitrogen,3,>)\n\n")
    
    result_text.insert(tk.END, "RIGHT ROOM:\n")
    result_text.insert(tk.END, "Row 1: #2(Blue/Deuterium,1,>)  #1(Yellow/Nitrogen,1,<)\n")
    result_text.insert(tk.END, "Row 2: #4(Yellow/Nitrogen,2,=)  #3(Green/Helium,1,=)\n")
    result_text.insert(tk.END, "Row 3: #6(Green/Helium,2,>)  #5(Blue/Deuterium,2,<)\n\n")
    
    result_text.insert(tk.END, "Pressure Key: > = ≥5783 psi, < = ≤5812 psi, = = 400 bar\n")
    result_text.insert(tk.END, "Color/Element Key: Blue=Deuterium, Green=Helium, Yellow=Nitrogen\n")
    result_text.insert(tk.END, "NOTE: Reactors 3, 4, and 10 (with = pressure) are NEVER correct!\n")

# Create main window
root = tk.Tk()
root.title("Payday 2: Big Oil Reactor Helper")
root.geometry("700x600")
root.resizable(True, True)

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10, "bold"))
style.configure("TCombobox", font=("Arial", 9))

# Title
title_label = ttk.Label(root, text="Payday 2: Big Oil Reactor Helper",
                        font=("Arial", 12, "bold"))
title_label.pack(pady=10)

# Input frame
input_frame = ttk.Frame(root)
input_frame.pack(pady=10, padx=20, fill="x")

# Chemical element (cylinder color) selection with elements in parentheses
ttk.Label(input_frame, text="Cylinder color:").grid(row=0, column=0, sticky="w", pady=5)
color_var = tk.StringVar()
color_combo = ttk.Combobox(input_frame, textvariable=color_var, state="readonly")
color_combo['values'] = ("Blue (Deuterium)", "Green (Helium)", "Yellow (Nitrogen)")
color_combo.grid(row=0, column=1, sticky="ew", pady=5, padx=5)

# Number of valves selection
ttk.Label(input_frame, text="Number of valves:").grid(row=1, column=0, sticky="w", pady=5)
valves_var = tk.StringVar()
valves_combo = ttk.Combobox(input_frame, textvariable=valves_var, state="readonly")
valves_combo['values'] = ("1 valve", "2 valves", "3 valves")
valves_combo.grid(row=1, column=1, sticky="ew", pady=5, padx=5)

# Pressure from monitor selection
ttk.Label(input_frame, text="Pressure from monitor:").grid(row=2, column=0, sticky="w", pady=5)
pressure_var = tk.StringVar()
pressure_combo = ttk.Combobox(input_frame, textvariable=pressure_var, state="readonly")
pressure_combo['values'] = ("≥5783 psi", "≤5812 psi")
pressure_combo.grid(row=2, column=1, sticky="ew", pady=5, padx=5)

# Configure column stretching
input_frame.columnconfigure(1, weight=1)

# Buttons frame
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

find_button = ttk.Button(button_frame, text="Find Correct Reactor", command=find_reactor)
find_button.grid(row=0, column=0, padx=5)

show_all_button = ttk.Button(button_frame, text="Show All Reactors", command=show_all_reactors)
show_all_button.grid(row=0, column=1, padx=5)

# Results text area
result_text = tk.Text(root, height=20, width=80, font=("Consolas", 9))
result_text.pack(pady=10, padx=20, fill="both", expand=True)

# Add scrollbar to text area
scrollbar = ttk.Scrollbar(result_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result_text.yview)

# Instructions at the bottom
instruction = """
Instructions:
1. Find notebooks in the house - determine cylinder color and number of valves
2. Check monitors in the lab - determine pressure (≥5783 or ≤5812 psi)
3. Select the found values and click "Find Correct Reactor"

Color to Element mapping:
- Blue = Deuterium
- Green = Helium  
- Yellow = Nitrogen

Important Notes:
- Reactors 3, 4, and 10 always have exactly 400 bar pressure and are NEVER correct
- Each reactor has fixed properties that don't change between game sessions
- Use "Show All Reactors" for quick reference
"""
instruction_label = ttk.Label(root, text=instruction, font=("Arial", 8), justify=tk.LEFT)
instruction_label.pack(pady=5)

# Start the application
root.mainloop()