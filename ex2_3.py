"""
необхідно створити програму для підрахунку днів у вказаному місяці 
та зазначити чи день є вихідним
"""
import calendar
data = "23-02-2020"
year = int(data[6:])
month = int(data[3:5])
day = int(data[:2])
#день тижня від 0 до 6, 6-неділя (day_week)
day_week = calendar.weekday(year,month,day)
# fist_day_week - перший день місяця(0-Пн .. 6-Нд), кількість днів в місяці - max_day_month
fist_day_week, max_day_month = calendar.monthrange(year,month)

Month = ["","січні","лютому","березні","квітні","травні","червні","липні",\
    "серпні","вересні","жовтні","листопаді","грудні"]
print(f"У {Month[month]} {year} року {max_day_month} день")
if day_week == 6:
    print(f"{data[:2]}.{data[3:5]}.{data[6:]} - вихідний")