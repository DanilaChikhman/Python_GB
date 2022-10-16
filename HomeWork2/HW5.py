# Реализовать алгоритм перемешивания списка.

import random

N = int(input("Введите размер списка: "))
spam = list(range(1, N+1))
print(spam)
random.shuffle(spam)
print(spam)
