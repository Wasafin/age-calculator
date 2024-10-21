import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        birth_date = datetime(year, month, day)
        today = datetime.now()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        # Display result
        messagebox.showinfo("Age Calculator", f"You are {age} years old.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid date values.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Labels and entry fields
tk.Label(root, text="Day:").grid(row=0, column=0)
day_entry = tk.Entry(root)
day_entry.grid(row=0, column=1)

tk.Label(root, text="Month:").grid(row=1, column=0)
month_entry = tk.Entry(root)
month_entry.grid(row=1, column=1)

tk.Label(root, text="Year:").grid(row=2, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1)

# Calculate button
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=3, column=1)

# Start the application
root.mainloop()
