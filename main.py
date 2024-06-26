import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organize_files():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory()

    files = os.listdir(directory)

    for file in files:
        filename, file_extension = os.path.splitext(file)

        if file_extension:
            file_extension_directory = os.path.join(directory, file_extension[1:])
            if not os.path.exists(file_extension_directory):
                os.makedirs(file_extension_directory)

            shutil.move(os.path.join(directory, file), os.path.join(file_extension_directory, file))

organize_files()