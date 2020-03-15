"""
необхідно створити програму для підрахунку днів у вказаному місяці 
та зазначити чи день є вихідним
"""
import calendar
data = "12-07-2019"
year = int(data[6:])
month = int(data[3:5])
day = int(data[:2])
print(year, month,day)
print(calendar.weekday(year,month,day))