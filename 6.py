num = int(input("Введите число: "))
is_even = 0
number = str(num)
while num > 0:
    num = num // 10
    is_even += 1
first_part = ''
second_part = ''
if is_even % 2 == 0:
    i = 0
    j = int(len(number) / 2)
    while i <= ((len(number) / 2) - 1):
        first_part = first_part + number[i]
        i += 1
    while j <= len(number) - 1:
        second_part = second_part + number[j]
        j += 1
    if first_part == second_part:
        print(number + '- полиндром.')
    else:
        print(number + '- не полиндром.')
else:
    i = 0
    j = int((len(number) + 1) / 2)
    while i <= ((len(number) - 1) / 2) - 1:
        first_part = first_part + number[i]
        i += 1
    while j <= len(number) - 1:
        second_part = second_part  + number[j]
        j += 1
    if first_part == second_part:
        print(number + '- полиндром.')
    else:
        print(number + '- не полиндром.')