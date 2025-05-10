import datetime as dt 

now = dt.datetime.now()
# print(now.date()) 
# print(now.time()) 
# print(now.month) 
# print(now.second) 

future = dt.datetime(2027, 6, 7, 12, 00)

# print(future - now)

# print(dt.datetime.strptime('3/5/27', '%d/%m/%y'))
# print(now.strftime('%d %b, %Y'))

"""
| Code | Meaning                        | Example      |
| ---- | ------------------------------ | ------------ |
| `%Y` | Year (4 digits)                | `2025`       |
| `%y` | Year (2 digits)                | `25`         |
| `%m` | Month (01 to 12)               | `05`         |
| `%B` | Full month name                | `May`        |
| `%b` | Abbreviated month name         | `May`        |
| `%d` | Day of the month (01 to 31)    | `10`         |
| `%H` | Hour (00 to 23)                | `14`         |
| `%I` | Hour (01 to 12)                | `02`         |
| `%p` | AM/PM                          | `PM`         |
| `%M` | Minute (00 to 59)              | `45`         |
| `%S` | Second (00 to 59)              | `09`         |
| `%f` | Microsecond (000000 to 999999) | `123456`     |
| `%z` | UTC offset                     | `+0200`      |
| `%Z` | Time zone name                 | `UTC`, `PST` |
| `%A` | Full weekday name              | `Saturday`   |
| `%a` | Abbreviated weekday name       | `Sat`        |
| `%j` | Day of the year (001 to 366)   | `130`        |
| `%W` | Week number                    |              |

"""

# pip install pygame
import pygame, time

pygame.init()
pygame.mixer.music.load(r"E:\Users\H p\Music\SQI.mp3")
# pygame.mixer.music.play()
# time.sleep(10)
# pygame.mixer.music.stop()

while True:
    now = dt.datetime.now()
    if now.strftime('%H') == '13' and now.strftime('%M') == '00' and now.strftime('%S') == '00':
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.stop()
    
            