import ttkbootstrap as ttk
import time
import datetime
from datetime import datetime, timedelta
from hijri_converter import convert
from prayer_times import read_prayer_times

class PrayerTimeGUI(ttk.Window):
    def __init__(self):

        # main window
        super().__init__(themename='darkly')
        self.attributes('-fullscreen', True)
        self.bind('<Escape>', lambda event: self.quit())
        self.configure(bg='black')

        # Frames
        self.main_top_frame = TopFrame(self)
        self.main_bottom_frame = BottomFrame(self)

    def run(self):
        self.mainloop()

class TopFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0,y=0, relheight=0.7, relwidth=1)
        self.create_widget()

    def create_widget(self):

        main_frame = ttk.Frame(self)
        background_label = ttk.Label(main_frame, background='#008028')

        data_frame = ttk.Frame(main_frame)

        clock_frame = ttk.Frame(data_frame)

        # Title label
        title_label = ttk.Label(clock_frame,
                          text='Muslim Student Association',
                          font=('Times New Roman', 45, 'italic'),
                          foreground='#008028',
                          anchor='s')

        # Live clock
        live_clock = ttk.Label(clock_frame, font=('Times New Roman', 200, 'bold'), foreground= '#FFE500', anchor = 'center')

        date = ttk.Label(clock_frame, font=('Helvetica', 20, 'bold', 'italic'), anchor='n', foreground='#008028')


        # Pack the live clock with padding

        def pack_widgets():

            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            title_label.pack(expand = True, padx =10)
            live_clock.pack(expand=True, fill = 'x',)
            date.pack(expand = True, fill = 'x', padx= 10)
            clock_frame.pack(side = 'left', expand = True, fill = 'both')
            data_frame.pack(expand = True, fill = 'both', padx= 15, pady=15)
            main_frame.pack(expand = True, fill = 'both', padx = 30, pady = 30)

        def digitalclock():

            current_time = time.strftime("%I:%M%p")

            if current_time[0] == '0':
                current_time = current_time[1:]

            live_clock.config(text=current_time)
            live_clock.after(1000, digitalclock)

        def live_date():

            current_date = datetime.now().strftime("%A, %B %d, %Y")

            hijri_date_obj = convert.Gregorian(datetime.now().year, datetime.now().month, datetime.now().day).to_hijri()
            hijri_date_str = f"{hijri_date_obj.day} {hijri_date_obj.month_name()} {hijri_date_obj.year} AH"

            date.config(text=f'{current_date} - {hijri_date_str}')

            date.after(1000, live_date)

        pack_widgets()
        digitalclock()
        live_date()

class BottomFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, rely=0.7, relheight=0.3, relwidth=1)
        self.prayer_times = read_prayer_times('prayertimes.csv')
        self.create_widgets()

    def create_widgets(self):
        def separator(parent):
            ttk.Separator(parent, style='light', orient='vertical').pack(side='left', expand=True, fill='both', pady=35)

        main_frame = ttk.Frame(self)
        background_label = ttk.Label(main_frame, background='#008028')
        prayer_times_frame = ttk.Frame(main_frame)

        # Fajr
        fajr = PrayerTimeEntry(prayer_times_frame, 'Fajr', "0")
        separator(prayer_times_frame)


        # Dhuhr
        dhuhr = PrayerTimeEntry(prayer_times_frame, 'Dhuhr',"0")
        separator(prayer_times_frame)

        # Asr
        asr = PrayerTimeEntry(prayer_times_frame, 'Asr', "0")
        separator(prayer_times_frame)

        # Maghrib
        maghrib = PrayerTimeEntry(prayer_times_frame, 'Maghrib', "0")
        separator(prayer_times_frame)

        # Isha
        isha = PrayerTimeEntry(prayer_times_frame, 'Isha', "0")


        def pack_widgets():

            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            main_frame.pack(expand=True, fill='both', padx=30, pady=30)
            prayer_times_frame.pack(expand=True, fill='both', padx=10, pady=10)

        def update_prayer_times():

            current_month = datetime.now().strftime('%B')
            current_day = datetime.now().strftime('%d')

            prayer_times = self.prayer_times[current_month][int(current_day)]

            fajr.update_time(prayer_times['Fajr'])
            dhuhr.update_time(prayer_times['Dhuhr'])
            asr.update_time(prayer_times['Asr'])
            maghrib.update_time(prayer_times['Magrib'])
            isha.update_time(prayer_times['Isha'])

            self.after(1000, update_prayer_times)

        def next_prayer_time():

            current_month = datetime.now().strftime('%B')
            current_day = datetime.now().strftime('%d')
            current_time = datetime.now()

            today_prayer_times = self.prayer_times[current_month][int(current_day)]
            tomorrow_prayer_times = self.prayer_times[current_month][int(current_day) + 1]

            time_format = "%I:%M %p"

            for prayer, prayer_time in today_prayer_times.items():

                prayer_time = datetime.strptime(prayer_time, time_format)

                prayer_time = prayer_time.replace(year=current_time.year, month=current_time.month, day=current_time.day)

                if prayer_time > current_time:
                    return prayer, prayer_time, prayer_time - current_time

            for prayer, prayer_time_str in tomorrow_prayer_times.items():

                prayer_time = datetime.strptime(prayer_time_str, time_format)
                prayer_time = prayer_time.replace(year=current_time.year, month=current_time.month, day= int(current_day) + 1)

                return prayer, prayer_time, prayer_time - current_time

        pack_widgets()
        next_prayer_time()
        update_prayer_times()

class PrayerTimeEntry(ttk.Frame):
    def __init__(self, parent, prayer_name, prayer_time):
        super().__init__(parent, style='light')
        self.pack(side='left', expand=True, fill='both')

        text_color = 'white'

        self.prayer_name_label = ttk.Label(self, text=prayer_name, font=('Times New Roman', 40, 'bold'), anchor='center', foreground=text_color)
        self.prayer_name_label.pack(expand=True, fill='both')

        self.prayer_time_label = ttk.Label(self, text=prayer_time, font=('Times New Roman', 40), anchor='center', foreground=text_color)
        self.prayer_time_label.pack(expand=True, fill='both')

        if prayer_name == 'Fajr':
            ttk.Label(self, text="Iqamah: 7:00AM", font=('Times New Roman', 13, 'bold'), anchor='center',foreground='grey').pack(expand=True, fill='both')

        if prayer_name == 'Dhuhr':
            ttk.Label(self, text="Iqamah: 2:00PM", font=('Times New Roman', 13, 'bold'), anchor='center', foreground='grey').pack(expand=True, fill='both')

        if prayer_name == 'Asr':
            ttk.Label(self, text="Iqamah: Asr + 10 minutes", font=('Times New Roman', 13, 'bold'), anchor='center', foreground='grey').pack(expand=True, fill='both')

        if prayer_name == 'Maghrib':
            ttk.Label(self, text="Iqamah: Maghrib + 5 minutes", font=('Times New Roman', 13, 'bold'), anchor='center', foreground='grey').pack(expand=True, fill='both')

        if prayer_name == 'Isha':
            ttk.Label(self, text="Iqamah: Isha + 10 minutes", font=('Times New Roman', 13, 'bold'), anchor='center', foreground='grey').pack(expand=True, fill='both')

    def update_time(self, new_prayer_time):
        self.prayer_time_label.config(text=new_prayer_time)


PrayerTimeGUI()


