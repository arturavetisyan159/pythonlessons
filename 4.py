# среднее арифметическое

i = int(input("Введите количество чисел последовательности: "))
a = i
sum = 0
max = float("-inf")
min = float("inf")

while i > 0:
    num = float(input("Введите число: "))
    if max < num:
        max = num
    if num < min:
        min = num
    sum = sum + num
    i -= 1
print("Среднее арифметическое равно", (sum/a))
print("Максимальное число равно", max)
print("Минимальное число ранво", min)