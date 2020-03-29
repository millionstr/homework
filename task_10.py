import json
import random
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

if __name__ == "__main__":
    #-----------------          основна прога          -------------------
    
    with open("prices.json", "r") as file:
        katalog = file.read()    
    baza = json.loads(katalog) # розпасили те що зчитали з файлу
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
    print("Вас обслуговує таксі ",taksi.name, "\nорієнтовна відстань до об'єкту ", taksi.distans, "км., \nорієнтовна вартість ", taksi.price(), "USD")

