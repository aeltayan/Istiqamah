import tkinter as tk
from tkinter import ttk

class PrayerTimeGUI(tk.Tk):

    def __init__(self):

        # main window
        super().__init__()
        self.attributes('-fullscreen', True)
        self.bind('<Escape>', lambda event: self.quit())

        # Frames
        self.main_top_frame = TopFrame(self)
        self.main_bottom_frame = BottomFrame(self)

    def run(self):

        self.mainloop()

class TopFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=0.7)
        ttk.Label(self, background='green').pack(expand = True, fill = 'both')
        ClockFrame(self)
        DateFrame(self)

class ClockFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, rely = 0.1, relwidth = 1, relheight = 1)
        ttk.Label(self, background="purple").pack(expand = True, fill = 'both')

class DateFrame(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth = 1, relheight = 0.1)
        ttk.Label(self, background='teal').pack(expand = True, fill = 'both')

class BottomFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, rely=0.7, relwidth=1, relheight=0.3)

        PrayerTimeFrame(self)
        JummahTimeFrame(self)

class PrayerTimeFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=0.9)

        PrayerTimeEntry(self, 'blue')
        PrayerTimeEntry(self, 'yellow')
        PrayerTimeEntry(self, 'blue')
        PrayerTimeEntry(self, 'yellow')
        PrayerTimeEntry(self, 'blue')


class JummahTimeFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, rely=0.8, relwidth=1, relheight=0.2)
        JummahTimeEntry(self)


class PrayerTimeEntry(ttk.Frame):
    def __init__(self, parent, background):
        super().__init__(parent)
        ttk.Label(self, background=background).pack(expand = True, fill = 'both')
        self.pack(side='left', expand = True, fill = 'both')

class JummahTimeEntry(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, background='orange').pack(expand = True, fill = 'both')
        self.pack(side='bottom', expand = True, fill = 'both')



PrayerTimeGUI()


