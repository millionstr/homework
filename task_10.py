"""
Створити програму, для виклику таксі

•	Користувач може вибрати такcі певної категорії зі списку (prices.json)

Приклад виводу переліку категорій у вигляді таблички:
Name	Estimate
UberX	$13-17
SUV	$50-64


•	Після, користувач може вказати назву категорії та відстань в кілометрах

•	Як результат на екран виводиться назва категорії таксі, 
відстань та ціна за цю відстань (При цьому ціна за кілометр розраховується випадковим чином
 на проміжку від high_estimate та low_estimate з prices.json)

•	Далі користувач має отримати повідомлення “Start” та при натиску на enter 
почнеться емуляція руху автівки автівки з відображенням пройденого шляху 
(див lesson 10 приклад з автомобілем)

•	Як тільки автівка пройде вказаний користувачем шлях, 
користувач має отримати повідомлення про прибуття та вартість поїздки
"""
import json
import random
import keyboard
import os
class Taksi:
    __price = None
    def __init__(self, name, distans, price_min, price_max):
        self.name = name
        self.distans = distans
        self.price_min = price_min
        self.price_max = price_max

    def price(self):
        __price = random.randint(self.price_min, self.price_max)*self.distans
        return __price

class Car:
    def __init__():
        pass


if __name__ == "__main__":
    #-----------------          основна прога          -------------------
    
    with open("prices.json", "r") as file:
        katalog = file.read()   # зчитуємо з файлу в змінну - katalog
    baza = json.loads(katalog) # розпасили те що зчитали з файлу; ^можна було baza =  json.loads(file)^
    number_of_services = len(baza['prices']) # кількість сервісів таксі
    print("Service", "   price per kilometer") # шапка таблиці
    services_taksi = list()
    for i in range(number_of_services): # виводимо список таксі з цінами
        if (baza['prices'][i]["currency_code"]):
            print(baza['prices'][i]["display_name"], end = "\t\t")
            print(baza['prices'][i]["estimate"])
            services_taksi.append(baza['prices'][i]["display_name"])

    while True:
        servis_taksi = input("виберіть будь-ласка службу таксі: ")
        if servis_taksi in services_taksi:
            break
        else:
            print("введіть корректно назву служби")
    
    while True:
        distance_in_kilometers = input("вкажіть орієнтовно відстань в кілометрах до об'єкту: ")
        if distance_in_kilometers.isdigit():
            distance_in_kilometers = int(distance_in_kilometers)
            break
        else:
            print("введіть корректно цифрами відстань")
            
    print()
    #print("distance_in_kilometers ",distance_in_kilometers)
    for i in range(number_of_services):
        if (baza['prices'][i]["display_name"] == servis_taksi):
            price_min = baza['prices'][i]["low_estimate"]
            price_max = baza['prices'][i]["high_estimate"]
    taksi = Taksi(servis_taksi, distance_in_kilometers, price_min, price_max)
    print("Вас обслуговує таксі: ",taksi.name, "\nорієнтовна відстань до об'єкту: ", taksi.distans, "км., \nорієнтовна вартість: ", taksi.price(), "USD")
    print("\nДля початку подорожі нажміть Enter \n**********START**********")
    keyboard.wait('enter') #while not(keyboard.is_pressed('enter')):
    os.system('CLS')  # очищає консоль
    
    print("ви натиснули <Enter>") 
