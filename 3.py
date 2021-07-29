# ЗАДАНИЕ 3: студенты с баллом выше среднего

num = int(input('Количество студентов: '))
students = {}
average_score = 0
for i in range(1, num + 1):
    name = input(str(i) + '-ый студент: ')
    score = int(input('Балл: '))
    average_score = average_score + score
    students.update([(name, score)])

average_score = average_score / num
round(average_score, 1)
print()

print('Средний балл:', average_score)

students_higher = []
stud_amount = 0
for stud in students:
    if students[stud] > average_score:
        stud_amount += 1
        students_higher.append(stud)
print('Студентов с баллом выше среднего:', stud_amount)
print(*students_higher)