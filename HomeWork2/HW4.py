# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры 

from random import Random, randint


N = int(input('Введите число N '))
numbers = []
numbers.append(range(-N,N,1))
i=-N
while i <= N: 
    numbers.append(i) #добавляет в список
    i+=1
print (numbers)


y1 = int(input('Укажите 1 позицию для вычисления - '))
y2 = int(input('Укажите 2 позицию для вычисления - '))
print("произведение: ")
print(numbers[y1]*numbers[y2])