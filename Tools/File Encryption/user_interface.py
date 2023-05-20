import tkinter as tk
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename()
    # Use the selected file for encryption/decryption?
    

def encrypt():
    # Perform encryption using selected file and key

def decrypt():
    # Perform decryption using selected file and key

# Example usage:
root = tk.Tk()
button = tk.Button(root, text='Select File', command=select_file)
button.pack()
root.mainloop()
