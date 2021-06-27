# максимальное из трех чисел

a = int(input())
b = int(input())
c = int(input())
maximum = a if (a >= b) and (a >= c) else (b if (b >= c) and (b >= a) else c)
print("Максимум из трех чисел:", maximum)