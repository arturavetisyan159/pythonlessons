N = int(input("N = "))
def even_sum (number):
    sum = 0
    while number != 0:
        if (number % 10) % 2 == 0:
            sum = sum + number % 10
        number = number // 10
    return sum
print("Сумма четных цифр в числе N =", even_sum(N))

def odd_sum (number):
    sum = 0
    while number != 0:
        if (number % 10) % 2 != 0:
            sum = sum + number % 10
        number = number // 10
    return sum
print("Сумма нечетных цифр в числе N =", odd_sum(N))