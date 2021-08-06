import tkinter as tk
from tkinter import filedialog

# Create
root = tk.Tk()
root.withdraw()

def loadSingleFile():
    file_path = filedialog.askopenfilename()
    print("loadSingleFile: ",file_path)
    return file_path

# For multiples files, name's'
# file_path = filedialog.askopenfilenames()




