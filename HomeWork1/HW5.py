""" Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21 """


def calculate(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5) # 
    return lengthSegment


arr = input("введите разделяя пробелом координаты 1 точки  ").split() # разбиение стринг пробелом
A = [int(item) for item in arr] # перевод каждый элемент списка в int
arr2 = input("введите разделяя пробелом координаты 2 точки  ").split()
B = [int(item) for item in arr2]
print(f"Длина отрезка: {format(calculate(A, B), '.2f')}")