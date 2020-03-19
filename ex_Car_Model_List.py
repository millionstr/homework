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

#print(" objectId ","\t", " Year ","\t", " Make ","\t", " Model ","\t", " Category ")
#print(ord("["), ord("{"), ord("\n"),ord(" "))
kilkist = 0
string = ""


def pars_key(i):# парсимо key
    stroka = ""
    print("while print i= ",i)
    while katalog[i] != ":":
        i+=1
        if katalog[i] != "\"":
            if (katalog[i]!="\n" and katalog[i]!=" "):
                print("if \"", katalog[i])
                stroka = stroka + katalog[i]
                print(stroka)
    else:
        key = stroka
        print("key = ", key[:-1])
        return (key[:-1],i)

def pars_value(i):# парсимо Value
    while 
    pass

def parse_dict(i):# парсимо словник
    
    while katalog[i] != "}":
        key_dict = pars_key(i)
        i=key_dict[1]
        print("key_dict, i", key_dict, katalog[i])
        pars_value(i)

        print("STOP")

#-----------------основна прога-------------------
with open("Car_Model_List.json", "r") as file:
    katalog = file.read()
valmas=len(katalog)
for i in range(valmas):
    if katalog[i] == "{":
        parse_dict(i) 
    else:
        print("else print: ",i, katalog[i], type(katalog[i]))