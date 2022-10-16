# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


s = str(input('введите число ')) # пишет стринг переводит в список
print(s)


if s.isalpha()==1:  # проверяет является ли буквой 1 ==тру
    print("ошибка это не число")
    exit()

s=int(s)

def factorial (s, count = 1):
    for i in range(1, s + 1):
        count *= i
    return count

for i in range(1, s + 1):
    if i == s: 
        print(f'{factorial(i)}')
    else:
        print(f'{factorial(i)}', end = ', ')