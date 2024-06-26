import tkinter as tk
import customtkinter as ctk
from tkinter import StringVar

# Function to read recipes from file
def read_recipes(filename):
    recipes = {}
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        current_recipe = None
        for line in lines:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            if line.endswith(':'):
                current_recipe = line[:-1]
                recipes[current_recipe] = {}
            elif current_recipe:
                parts = line.split(':')
                if len(parts) == 2:  # Ensure the line contains exactly one ':'
                    ingredient, quantity = parts
                    recipes[current_recipe][ingredient.strip()] = float(quantity.strip())
    return recipes

# Function to handle calculations and display results
def calculate_ingredients():
    selected_recipe = selected_option.get()
    if selected_recipe == "Wybierz Przepis.":
        result_label.configure(text="Wybierz Przepis.")
        return

    try:
        desired_quantity = float(quantity_entry.get())
        ingredients = recipes[selected_recipe]
        result_text = f"Dla {desired_quantity} kg {selected_recipe}, potrzebujesz:\n"
        for ingredient, base_quantity in ingredients.items():
            total_quantity = base_quantity * desired_quantity
            formatted_quantity = "{:.2f}".format(total_quantity)  # Format to two decimal places
            result_text += f"{ingredient}: {formatted_quantity} kg\n"
        result_label.configure(text=result_text)
    except ValueError:
        result_label.configure(text="Wpisz poprawną wartość.")

# System settings
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Application frame
app = ctk.CTk()
app.geometry("1920x1080")
app.title("Przelicznik przepisów")
app.configure(bg="#FCD400")  # Change background color of the main window

# Read recipes from file
recipes = read_recipes('recipes.txt')
recipe_names = list(recipes.keys())

# Top frame
top_frame = ctk.CTkFrame(app)
top_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(20, 20))
top_frame.configure(fg_color="#FCD400")  # Change background color of the top frame

# Add UI elements
title = ctk.CTkLabel(top_frame, text="Wybierz przepis", font=("Arial", 40, "bold"))
title.pack(pady=(20, 10))
title.configure(fg_color="#FCD400")  # Change background color of the label

selected_option = StringVar(app)
selected_option.set("Lista Przepisów")  # Default value

# Create ComboBox with CTkComboBox for better appearance
combo_box = ctk.CTkComboBox(top_frame, variable=selected_option, values=recipe_names)
combo_box.pack(pady=(10, 20))

# Label for user input
quantity_label = ctk.CTkLabel(top_frame, text="Podaj liczbę, ile kg gotowego produktu ma wyjść:", font=("Arial", 24, "bold"))
quantity_label.pack(pady=(20, 5))
quantity_label.configure(fg_color="#FCD400")  # Change background color of the label

quantity_entry = ctk.CTkEntry(top_frame)
quantity_entry.pack(pady=5)

# Set application icon
app.iconbitmap('icon.ico')  # Provide path to your icon

# Button to calculate ingredients
calculate_button = ctk.CTkButton(top_frame, text="Przelicz", text_color="white",font=("Arial",16,"bold"),command=calculate_ingredients)
calculate_button.pack(pady=20, padx=10)
calculate_button.configure(fg_color="#c20f24", hover_color="#720915")  # Change colors as needed

# Label to display result
result_label = ctk.CTkLabel(app, text="", font=("Arial", 62))
result_label.pack(pady=10)

# Start Tkinter event loop
app.mainloop()
