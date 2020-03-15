"""
створити програму для генерації випадкового масиву чисел.
масив має бути створений випадковими числами (розмір 20 елементів)
    - програма має визначати скільки елементів масиву дорівнює числу введеному користувачем
    - кожне друге число має бути від'ємне.
    - визначити скільки елементів масиву дорівнюють числу введеному користувачем.
"""
import random
lists = list()
for i in range(10):
    lists.append(random.randint(-10,-1))
    lists.append(random.randint(1,10))
print(lists, len(lists))

namber = int(input("введіть ціле число: "))
repeat_namber=0
for i in lists:
    if i == namber:
        repeat_namber += 1
print(f"число {namber} повторюється в масиві {repeat_namber} разів")
