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
    stroka = ""
    i=i+1
    while katalog[i] != ",":
        if katalog[i] != "}":
            stroka = stroka + katalog[i]
            i += 1
    stroka = stroka.strip()
    stroka = stroka.strip("\"")
    print("pars_value - strpka ",stroka)
    return (stroka, i)

def parse_dict(i):# парсимо словник
    single_dict = {}
    while katalog[i] != "}":
        key_dict = pars_key(i)
        i=key_dict[1]
        print("key_dict, i", key_dict, katalog[i])
        value_dict = pars_value(i)
        i=value_dict[1]
        single_dict[key_dict[0]]=value_dict[0]
        print("рядок словника-",single_dict)
        print("STOP")
    return (single_dict, i)

#-----------------основна прога-------------------
with open("Car_Model_List.json", "r") as file:
    katalog = file.read()
valmas=len(katalog)
Car_Model_List=[]
for i in range(valmas):
    if katalog[i] == "{":
         end_dict=parse_dict(i)
         i = end_dict[1]
         Car_Model_List.append(end_dict[0])
         print("Car_Model_List ",Car_Model_List)
         print("STOP ALL")
        
    else:
        print("else print: ",i, katalog[i], type(katalog[i]))