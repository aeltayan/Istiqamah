import time
import datetime
from datetime import datetime
from hijri_converter import convert
class DynamicUpdater:
    def update_clock(self, live_clock):

        current_time = time.strftime("%I:%M %p")
        if current_time[0] == '0':
            current_time = current_time[1:]

        live_clock.config(text=current_time)
        live_clock.after(1000, lambda: self.update_clock(live_clock))

    def update_date(self, live_date):

        current_date = datetime.now().strftime("%A, %B %d, %Y")

        hijri_date_obj = convert.Gregorian(datetime.now().year, datetime.now().month, datetime.now().day).to_hijri()
        hijri_date_str = f"{hijri_date_obj.day} {hijri_date_obj.month_name()} {hijri_date_obj.year} AH"

        live_date.config(text=f'{current_date} - {hijri_date_str}')
        live_date.after(1000, lambda : self.update_date(live_date))


    def update_prayer_times(self, parent_widget, prayer_times, prayer_time_entries):

        current_month = datetime.now().strftime('%B')
        current_day = datetime.now().strftime('%d')

        today_prayer_times = prayer_times[current_month][int(current_day)]

        prayer_time_entries['Fajr'].update_time(today_prayer_times['Fajr'])
        prayer_time_entries['Dhuhr'].update_time(today_prayer_times['Dhuhr'])
        prayer_time_entries['Asr'].update_time(today_prayer_times['Asr'])
        prayer_time_entries['Maghrib'].update_time(today_prayer_times['Magrib'])
        prayer_time_entries['Isha'].update_time(today_prayer_times['Isha'])

        parent_widget.after(1000, lambda : self.update_prayer_times(parent_widget, prayer_times, prayer_time_entries))


    def countdown(self, countdown_label, time_difference, next_prayer):

        time_difference = time_difference - 1

        hours, remainder = divmod(time_difference, 3600)
        minutes, seconds = divmod(remainder, 60)

        countdown_str = f"{next_prayer} in:{int(hours):2}:{int(minutes):02}:{int(seconds):02}"

        countdown_label.config(text = countdown_str)

        countdown_label.after(1000, lambda : self.countdown(countdown_label, time_difference, next_prayer))