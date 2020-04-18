"""
----------********** РІШЕННЯ СУДОКУ **********----------
mas = [[0,0,0,5,4,3,0,0,0],[0,0,2,0,0,0,8,0,0],[0,4,0,0,0,0,0,9,0],[9,0,0,1,6,2,0,0,7],[8,0,0,4,0,9,0,0,1],[4,0,0,7,5,8,0,0,6],[0,5,0,0,0,0,0,6,0],[0,0,8,0,0,0,2,0,0],[0,0,0,8,7,6,0,0,0]]
це складний рівень задачі
"""
mas = [[2,0,0,0,9,0,0,0,8],[0,5,3,1,8,7,2,6,0],[0,8,0,2,0,6,0,3,0],[0,7,5,3,0,2,1,8,0],[4,1,0,0,0,0,0,7,2],[0,2,9,7,0,8,6,4,0],[0,4,0,6,0,9,0,1,0],[0,9,6,5,3,1,4,2,0],[1,0,0,0,2,0,0,0,6]]

def p_mas(mas):
    """ роздруковує масив """
    len_mas1 = len(mas)
    for i in range(len_mas1):
        print(mas[i])

def auxiliary_mas(mas1):
    """ бере mas1 переставляє строки в стовпці і присвоює масиву mas2 """        
    mas2=list()
    j=list()
    len_mas1_x = len(mas1) # кількість строк в mas1
    len_mas1_y = len(mas1[0]) # кількість елементів в строкі в mas1
    for i in range(len_mas1_x):
        j=mas1[i].copy()
        mas2.append(j)
   
    for i1 in range(len_mas1_x):
        for j1 in range(len_mas1_y):
            mas2[j1][i1] = mas1[i1][j1]

    return (mas2)

class Nine:
    """ екземпляр класу містить список індексів окремої матриці 3х3 """
    def __init__(self,x1,y1): #х1, у1 - це координати верхнього лівого елементу
        self.x1 = x1
        self.y1 = y1
        self.nine = list()
        for x in range(self.x1,self.x1+3):
            for y in range(self.y1,self.y1+3):
                self.nine.append([x,y])
        #print(self.nine)


if __name__ == "__main__":
        
    p_mas(mas)
    mark = True
    help_second_mas = auxiliary_mas(mas)
    print("------------------------------------------")
    #p_mas(help_second_mas)
    index_list=list() # містить індекси елементів окремих матриць 3х3
    for i in range(0,9,3):
        for j in range(0,9,3):
            matr = Nine(i,j)
            index_list.append(matr)
    
    for i in range(9): # друк індексів
        print(index_list[4].nine[i], end=" ")
        if i==2 or i==5:
            print()
    print()
    for i in range(9): # друк комірки 3х3
        temp = index_list[4].nine[i]
        print(mas[temp[0]][temp[1]], end = " ")
        if i==2 or i==5:
            print()
"""    for i in range(81): # запускаємо підпрограму для кожного 81 елемента масива
        if mas is defmas(mas):
"""