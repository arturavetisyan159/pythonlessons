# калькулятор

print("Выберите опреацию: ")
print("1 - \"r\" - применяет унарный минус к опреанду")
print("2 - \"+\" - сложение")
print("3 - \"-\" - вычитание")
print("4 - \"/\" - деление")
print("5 - \"*\" - умножение")
print("6 - \"%\" - деление по модулю")
print("7 - \"<\" - минимальное из двух чисел")
print("8 - \">\" - максимальное из двух чисел")

operation = int(input("Введите цифру: "))

if operation == 1:
    num = int(input("Введите число: "))
    if num == 0:
        print("К 0 такая операция неприменима.")
    else:
        print("Ответ:", -num)
elif operation == 2:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print('Ответ:', (num1 + num2))
elif operation == 3:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print('Ответ:', (num1 - num2))
elif operation == 4:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    if num2 != 0:
        print('Ответ:', (num1 / num2))
    else:
        print('На ноль делить нельзя!')
elif operation == 5:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print('Ответ:', (num1 * num2))
elif operation == 6:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print('Ответ:', (num1 % num2))
elif operation == 7:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    if num1 == num2:
        print("Числа равны.")
    elif num1 > num2:
        print("Минимальное число:", num2)
    else:
        print("Минимальное число: ", num1)
elif operation == 8:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    if num1 == num2:
        print("Числа равны.")
    elif num1 > num2:
        print("Максиимальное число:", num1)
    else:
        print("Максиимальное число: ", num2)
