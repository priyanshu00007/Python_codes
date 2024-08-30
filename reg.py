import tkinter as tk
from tkinter import messagebox

def register():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    
    # Validate inputs
    if not username or not password or not email:
        messagebox.showerror("Error", "Please fill all fields")
        return
    
    # Register user (simulated)
    print("Registered successfully!")
    print("Username:", username)
    print("Password:", password)
    print("Email:", email)
    
    # Clear fields
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_email.delete(0, tk.END)

root = tk.Tk()
root.title("Registration Window")

label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=10)

entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=10)

button_register = tk.Button(root, text="Register", command=register)
button_register.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()