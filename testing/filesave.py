import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Ask the user to select a file to save
file_path = filedialog.asksaveasfilename(defaultextension='.txt')

if file_path:
    # Save the file
    with open(file_path, 'w') as f:
        f.write('Hello, world!')