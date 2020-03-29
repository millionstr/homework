import json
"""class Taksi:
    def __init__(name, estimate):
        self.name = name
        self.estimate = estimate
"""

if __name__ == "__main__":
    #-----------------          основна прога          -------------------
    
    with open("prices.json", "r") as file:
        katalog = file.read()    
    baza = json.loads(katalog) # розпасили те що зчитали з файлу
    number_of_services = len(baza['prices']) # кількість сервісів таксі
    print("Service", "   price per kilometer") # шапка таблиці
    services_taksi = list()
    for i in range(number_of_services):
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

