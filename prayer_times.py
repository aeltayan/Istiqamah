import csv

def read_prayer_times(filename: str):

    prayer_times = {}
    current_month = None

    with open(filename, mode='r') as file:

        csv_reader = csv.reader(file)

        for row in csv_reader:
            if any(month in row for month in ['January', 'February', 'March', 'April', 'May', 'June',
                                              'July', 'August', 'September', 'October', 'November', 'December']):
                current_month = row[1]
                if current_month not in prayer_times:
                    prayer_times[current_month] = {}

            elif row[0] and current_month:
                prayer_times[current_month][int(row[1])] = {
                    'Fajr': row[2],
                    'Sunrise': row[3],
                    'Dhuhr': row[4],
                    'Asr': row[5],
                    'Magrib': row[6],
                    'Isha': row[7]
                }

    return prayer_times
