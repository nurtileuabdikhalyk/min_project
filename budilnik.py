import datetime
from playsound import playsound
from time import sleep
import sys

time_now = datetime.datetime.now()
print(time_now)
day = input('День: ')
hour = input('Час: ')
minutes = input('Минуты: ')
if 1 > int(day) or int(day) > 31 or 0 > int(hour) or int(hour) > 59 or 0 > int(minutes) or int(minutes) > 59:
    sys.exit()
if len(day) == 1:
    day = '0' + day
if len(hour) == 1:
    hour = '0' + hour
if len(minutes) == 1:
    minutes = '0' + minutes
while True:
    time_now = datetime.datetime.now()
    if str(time_now.day) == day and str(time_now.hour) == hour and str(time_now.minute) == minutes:
        playsound('D:\\muz.mp3')
        break
    sleep(1)
