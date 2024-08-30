import tkinter as tk
from tkinter import ttk

# List of cities
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

# Create the main window
root = tk.Tk()
root.title("City Selection")

# Create a Tkinter variable to store the selected city
selected_city = tk.StringVar()

# Create the dropdown list
city_dropdown = ttk.Combobox(root, textvariable=selected_city)
city_dropdown['values'] = cities
city_dropdown['state'] = 'readonly'  # Optional: Make the dropdown read-only
city_dropdown.current(0)  # Set the default selected city
city_dropdown.pack(pady=20)

# Function to handle city selection
def city_selected():
    print("Selected City:", selected_city.get())

# Button to trigger city selection
select_button = tk.Button(root, text="Select City", command=city_selected)
select_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
