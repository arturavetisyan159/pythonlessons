# Сортировка сначала по имени, потом по баллам.

students = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]

students.sort(key=lambda el: el['name'])
print(students)

students.sort(key=lambda el: el['final'], reverse=True)
print(students)
