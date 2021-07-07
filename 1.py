# есть ли элемент в списке

is_exist = False
my_list = []

n = int(input("n= "))
for i in range(0, n):
    element = int(input("=> "))
    my_list.append(element)

print("Введите число: ")
ch = int(input("ch= "))

for el in my_list:
    if el == ch:
        is_exist = True

if is_exist == True:
    print("Введенное число есть в списке!")
elif is_exist == False:
    print("Введенного числа в списке нет!")
