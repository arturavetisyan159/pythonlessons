# Нечетные числа в указанном диапазоне

a = int(input("Введите 1-ое число: "))
b = int(input("Введите 2-ое число: "))

for i in range(a, b + 1):
    if i % 2 == 0:
        continue
    else:
        print(i, end=" ")