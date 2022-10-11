""" for i in range(10):
    a=i
    print(a) """

    # напишите программу которая принимает два числа, проверяет является ли одно квадратом другог
    # 5, 25 - да

""" print("введите два числа")
a=int(input())
b=int(input())
if a>=b:
    if a==b**2:
        print("квадрат первого")
    else :
        print("no")
elif b>a:
    if b==a**2:
        print("квадрат вторго")
    else :
        print("no")
else:
    print("не является") """

""" 
#программа на вход принимает 5 чисел находит меньшее
def input_list():
  count=int(input('how many element: '))
  return [int(input()) for _ in range(count)] #короткая запись генератор случайных чисел

nums = input_list()
max_num = nums[0]
for i in nums:
    if i>max_num:
        max_num = i
    
print(f'max is {max_num}')

 """

""" 
 #программа принимает N выводит от -Н до Н

N=int(input("введите N "))

for i in range(-N, N+1):
    print(i)

 """

""" 
 #на вход принимается дробь и показывает первую часть дробного числа
a = float(input())
result = (a*10)%10
if result == 0:
    print("не дробь")
else:
    print(int(result))
 """

#программа принимает число проверяет кратно 5и10, 15 но не 30

a= int (input("введите число "))
if a%5==0 and a%10 ==0:
    print("кратно 10 и 15")
elif a%15==0 and a%30!=0:
    print("кратно 15 не кратно 30")
else:
    print("не соответствует ")


