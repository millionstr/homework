"""
необхідно створити додаток, для обробки інформації з автокаталогу

1. зчитати дані з вхідного файлу Car_Model_List.json та вивести на екран
* бажано не використовувати сторонні бібліотеки

2.1 вивести список доступних брендів авто
2.2 вивести список моделей вказаного бренду користувачем
2.3 пошук моделі по імені
2.4 знайти усі моделі виробника за вказаний проміжок часу

результат має бути відображеним у формі таблички
"objectId": "cptB1C1NSL",
"Year": 2020,
"Make": "Audi",
"Model": "Q3",
"Category": "SUV",
"createdAt": "2020-01-27T20:44:17.665Z",
"""
# tmp = file.read(6) читає перші 6 символів
specSymbols = ("[" , "]" , "{" , "}" , "," , "\n", " ")


#print(ord("["), ord("{"), ord("\n"),ord(" "))
kilkist = 0
string = ""


def pars_key(i):# парсимо key
    stroka = ""
    #print("while print i= ",i)
    while katalog[i] != ":":
        i+=1
        if katalog[i] != "\"":
            if (katalog[i]!="\n" and katalog[i]!=" "):
                #print("if \"", katalog[i])
                stroka = stroka + katalog[i]
                #print(stroka)
    else:
        key = stroka
        #print("key = ", key[:-1])
        return (key[:-1],i)

def pars_value(i):# парсимо Value
    stroka = ""
    i=i+1
    while katalog[i] != ",":
        if katalog[i] != "}":
            stroka = stroka + katalog[i]
            i += 1
        else:
            break
    stroka = stroka.strip()
    stroka = stroka.strip("\"")
    #stroka = stroka.strip("}")
    #print("pars_value - strpka ",stroka)
    return (stroka, i)

def parse_dict(i):# складаємо словник
    single_dict = {}
    while katalog[i] != "}":
        key_dict = pars_key(i)
        i=key_dict[1]
        #print("key_dict, i", key_dict, katalog[i])
        value_dict = pars_value(i)
        i=value_dict[1]
        single_dict[key_dict[0]]=value_dict[0]
        #print("рядок словника-",single_dict)
        #print("STOP")
    return (single_dict, i+1)

#-----------------основна прога-------------------
with open("Car_Model_List_all.json", "r") as file:
    katalog = file.read()
valmas=len(katalog)-1
Car_Model_List=[]
i = 0
while i< valmas:
    i += 1
    if katalog[i] == "{":
         end_dict=parse_dict(i)
         i = end_dict[1]
         Car_Model_List.append(end_dict[0])
         #print("Car_Model_List ",Car_Model_List)
         #print("STOP ALL")
        
    else:
        pass
        #print("else print: ",i, katalog[i], type(katalog[i]))
print("парсинг закінчено")
print(" objectId ","\t", " Year ","\t", " Make ","\t", " Model ","\t", " Category ")
for i in Car_Model_List:
    print(f"{i['Make']}, {i['Year']},{i['Model']}")

print("LEVEL 2")
while True:
    print("1. Вивести список доступних брендів.\n\
        2. Вивести список моделей вказаного бренду.\n\
        3. Пошук моделі по імені.\n\
        4. Знайти всі моделі виробника за вказаний проміжок часу.\n\
        5. Вийти зменю. \n")
    menu_namber = input("виберіть пункт меню (введіть ціле число від 1 до 5): ")
    if menu_namber.isdigit():
        if menu_namber == "5":
            break
        elif menu_namber == "1": 
            print("ввели 1")
        elif menu_namber == "2":
            print("ввели 2")
        elif menu_namber == "3":
            print("ввели 3")
        elif menu_namber == "4":
            print("ввели 4")
        else:
            print("ви ввели число не з діапазону 1..5")
            continue
    else:
        print("Помилка, введіть правильно число")