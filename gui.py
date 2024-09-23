import tkinter as tk
from tkinter import ttk

class PrayerTimeGUI:

    def __init__(self):

        self.window = tk.Tk()
        self.window.attributes("-fullscreen", True)
        self.window.bind('<Escape>', lambda event: self.window.quit())

        self.layout()

    def layout(self):

        pass

    def create_widgets(self):

        pass


    def run(self):

        self.window.mainloop()

