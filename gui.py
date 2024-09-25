import tkinter as tk
from tkinter import ttk
from prayer_times import read_prayer_times

class PrayerTimeGUI:

    def __init__(self):

        self.window = tk.Tk()
        self.window.attributes("-fullscreen", True)
        self.window.bind('<Escape>', lambda event: self.window.quit())
        self.prayer_times = read_prayer_times('prayertimes.csv')

        self.frame_layout()

    def frame_layout(self):

        main_top_frame = ttk.Frame(self.window, borderwidth=20, relief= tk.GROOVE)
        main_top_frame.pack(fill='both', expand = True)

        main_bottom_frame = ttk.Frame(self.window, borderwidth=20, relief= tk.GROOVE)
        main_bottom_frame.pack(fill='both', expand = True)


    def create_widgets(self):

        pass


    def run(self):

        self.window.mainloop()


