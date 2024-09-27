import ttkbootstrap as ttk
import time
from time import strftime
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

class PrayerTimeGUI(ttk.Window):

    def __init__(self):

        # main window
        super().__init__(themename='darkly')
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
        self.place(x=0,y=0, relheight=0.7, relwidth=1)
        self.create_clock()


    def create_clock(self):
        # Title label
        label = ttk.Label(self, text='Muslim Student Association', font=('Segoe UI', 40, 'bold'), anchor='center', style='success')

        # Frame for clock display
        clock_frame = ttk.LabelFrame(self, labelwidget=label, padding=20, style='success')

        # Live clock display
        live_clock = ttk.Label(
            clock_frame,
            font=('Segoe UI', 200, 'bold'),
            style='success',
            anchor='center'
        )

        # Pack the live clock with padding
        live_clock.pack(expand=True, fill='both', padx=20, pady=20)

        # Pack the clock frame with padding
        clock_frame.pack(expand=True, fill='both', padx=30, pady=30)

        def digitalclock():

            current_time = time.strftime("%I:%M%p")

            if current_time[0] == '0':
                current_time = current_time[1:]

            live_clock.config(text=current_time)
            label.after(1000, digitalclock)

        digitalclock()



class BottomFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, rely=0.7, relheight=0.3, relwidth=1)







PrayerTimeGUI()


