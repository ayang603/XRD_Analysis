import os

import tkinter as tk
import tkinter.font

from tkinter import messagebox
from tkinter.filedialog import askdirectory


def extract():
    data = None

    return data

class App:

    def __init__(self):
        # Create Windows
        self.window = tk.Tk()
        self.window.title("XRD Analysis")
        self.directory = os.getcwd()

        # Windows Setting
        self.window.geometry("860x360")
        self.window.resizable(width=False, height=False)
        self.w_font = tkinter.font.nametofont("TkDefaultFont")
        self.w_font.config(size=9)

        self.left = tk.Frame(self.window, width=240, height=340)
        self.left.grid(row=0, column=0, padx=10, pady=10)

        self.right = tk.Frame(self.window, width=580, height=340)
        self.right.grid(row=0, column=1, padx=10, pady=10)

        self.main_frame = tk.Frame(self.left, width=240, height=160)
        self.main_frame.grid(row=0, column=0)

        #self.title_frame = tk.Frame(self.main_frame, width=240, height=320, highlightbackground="black",
        #                            highlightthickness=1)
        #self.title_frame.grid(row=0, column=0, pady=10)

        self.folder_frame = tk.Frame(self.main_frame, width=240, height=20)
        self.folder_frame.grid(row=1, column=0)

        # Labels
        self.title = tk.Label(self.main_frame, text="XRD Analysis", font=("Courier", 20, "bold"))
        self.title.grid(row=0, column=0)


        # Data
        self.data_raw = None

        # Buttons
        def chg_dir():
            path = askdirectory()
            self.dir.config(text=path)
            os.chdir(path)

            self.data_raw = extract()




            if self.data is None:
                messagebox.showerror("No Files Found", "Please choose a different directory.")

        self.window.mainloop()




if __name__ == "__main__":
    # Runs Application
    App()
