import tkinter as tk
from tkinter import messagebox
import math

class AreaCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Area Calculator")
        
        self.shape_var = tk.StringVar(value="Triangle")
        self.dimensions = {}
        
        self.create_widgets()

    def create_widgets(self):
        # Shape selection dropdown
        tk.Label(self.root, text="Select Shape:").grid(row=0, column=0, pady=5)
        tk.OptionMenu(self.root, self.shape_var, "Triangle", "Rectangle/Square", "Circle", command=self.update_fields).grid(row=0, column=1, pady=5)
        
        # Input fields frame
        self.input_frame = tk.Frame(self.root)
        self.input_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.update_fields()  # Initialize fields

        # Calculate button
        tk.Button(self.root, text="Calculate Area", command=self.calculate_area).grid(row=2, column=0, columnspan=2, pady=10)

        # Output label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"))
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def update_fields(self, *args):
        # Clear previous input fields
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        self.dimensions.clear()
        shape = self.shape_var.get()

        if shape == "Triangle":
            self.add_input_field("Base", "base")
            self.add_input_field("Height", "height")
        elif shape == "Rectangle/Square":
            self.add_input_field("Length", "length")
            self.add_input_field("Width", "width")
        elif shape == "Circle":
            self.add_input_field("Radius", "radius")

    def add_input_field(self, label, key):
        tk.Label(self.input_frame, text=f"{label}:").pack(anchor="w")
        entry = tk.Entry(self.input_frame)
        entry.pack(fill="x", padx=5, pady=2)
        self.dimensions[key] = entry

    def calculate_area(self):
        shape = self.shape_var.get()
        try:
            if shape == "Triangle":
                base = float(self.dimensions["base"].get())
                height = float(self.dimensions["height"].get())
                area = (base * height) / 2
            elif shape == "Rectangle/Square":
                length = float(self.dimensions["length"].get())
                width = float(self.dimensions["width"].get())
                area = length * width
            elif shape == "Circle":
                radius = float(self.dimensions["radius"].get())
                area = math.pi * radius**2
            else:
                raise ValueError("Unsupported shape")

            self.result_label.config(text=f"Area: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AreaCalculator(root)
    root.mainloop()
