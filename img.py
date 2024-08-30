import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Image Display")

# Load the image
image = Image.open("batman.jpg")  # Provide the full path
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(root, image=photo)
label.pack()

# Run the application
root.mainloop()
