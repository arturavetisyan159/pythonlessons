# Слово "Копеек" в нужном формате.

num = int(input('Введите число от 1 до 99: '))
if (5 <= num) and (num <= 20):
    print(num, 'копеек')
else:
    if num % 10 == 1:
        print(num, 'копейка')
    elif num % 10 == 2 or num % 10 == 3 or num % 10 == 4:
        print(num, 'копейки')
    else:
        print(num, 'копеек')
