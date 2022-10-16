# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11




s = list(map(str,input('введите число ') ))
s = [item.replace(",", "") for item in s]
print(s)
s=list(filter(None, s))
print(s)
s=list(map(int, s))
print(s)
s=sum(s)
print(s)



