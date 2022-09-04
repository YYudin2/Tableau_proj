import datetime
import csv
from suntime import Sun, SunTimeException

latitude = 50.45
longitude = 30.5233

sun = Sun(latitude, longitude)

names = ['month', 'day', 'sunrise_hour', 'sunrise_minute','sunset_hour', 'sunset_minute']

lt = []
i = 0
date = datetime.date(2020, 1, 1)
while date <= datetime.date(2020, 12, 31):
    lt.append({names[0]: date.month, names[1]: date.day, names[2]: sun.get_local_sunrise_time(date).hour,
               names[3]: sun.get_local_sunrise_time(date).minute, names[4]: sun.get_local_sunset_time(date).hour,
               names[5]: sun.get_local_sunset_time(date).minute})
    # print (lt[i])
    i += 1
    date = date + datetime.timedelta(days=1)

with open('sun.csv', 'w', newline='') as sun_csv:
    writer = csv.DictWriter(sun_csv, fieldnames= names)
    writer.writeheader()
    writer.writerows(lt)
