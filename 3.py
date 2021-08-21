# Задача 3: возведите в квадрат и потом в куб элементы списка.

nums = [3, 5, 7, 3, 9, 5, 7, 2]

square = list(map((lambda x: x**2), nums))
print(square)
cube = list(map((lambda x: x**3), nums))
print(cube)

