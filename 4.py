# Получить минимальную и максимальную итоговую оценки студентов.

students = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]

students.sort(key=lambda el: el['final'], reverse=True)

print(students[0])
print(students[len(students) - 1])
