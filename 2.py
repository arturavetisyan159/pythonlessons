# Отгадать число от 1 до 100
import math

a = 84
infinity = math.inf

count = 1

for i in range(1, 100):
    b = int(input("Введите число в диапазоне от 1 до 100: "))
    if a == b:
        print("Число угадано с", count, "раза")
        break
    else:
        if a > b:
            print("Загаданное число больше введенного! \n")
        else:
            print("Загаданное число меньше введенного")
    count += 1