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


#программа на вход принимает 5 чисел находит меньшее
def input_list():
  count=int(input('how many element: '))
  return [int(input()) for _ in range(count)] #короткая запись

nums = input_list()
max_num = nums[0]
for i in nums:
    if i>max_num:
        max_num = i
    
print(f'max is {max_num}')

