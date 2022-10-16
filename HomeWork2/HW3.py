# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# *Пример:*

#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06


from ast import While

s = str(input('введите число ')) 
print(s)

if s.isalpha()==1:  # проверяет является ли буквой 1 ==тру
    print("ошибка. это не число")
    exit()

s=int(s)
i=int(1)
arr = []
while i <= s: 
    x=(1+1/i)**i
    # print ( x)
    i+=1
    x=round(x,2) #округление до 2х
    arr.append(x) #добавляет в список

print(arr)
print(sum(arr))