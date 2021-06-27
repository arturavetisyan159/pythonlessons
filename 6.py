# Вывод символа

n = int(input("Введите количество символов: "))
symbol = input("Введите символ: ")
print("0 - Горизонтальная")
print("1 - Вертикальная")
orientation = int(input("Выберите ориентацию: "))

if orientation == 0:
     while n > 0:
         print(symbol, end=" ")
         n -= 1
elif orientation == 1:
    while n > 0:
        print(symbol)
        n -= 1
else:
    print("Неправильно выбрана ориентация!")