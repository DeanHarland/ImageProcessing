import tkinter as tk
from tkinter import filedialog

# Create
root = tk.Tk()
root.withdraw()

def loadSingleFile():
    file_path = filedialog.askopenfilename()
    return file_path


def loadMultipleFiles():
    file_path = filedialog.askopenfilenames()
    return file_path


