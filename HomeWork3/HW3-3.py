# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

s = int(input('введите колличество элементов в списке ')) 
# print(s)
i = 0
arr =[]
while i <= s-1:
    r =round(random.uniform(0.5, 10.5), 2) #генерация дробных и округление
    arr.append(r)
    #print(r)
    i=i+1
print(f'список {arr}')
arr2=[]
i=0
while i <= s-1:
    r=round(arr[i], 0)
    #print(r)
    x=round(arr[i]-r,2)
    arr2.append(x)
    i=i+1
print(f'дробная часть {arr2}')
element = max (arr2)-min(arr2)
print(f'ответ {element}')


