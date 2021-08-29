s = 'I am learning Python. hello WORLD!'
str_list = s.split('h')
stroka = ''

for i in range(1, len(str_list) - 1):
    stroka = stroka + str_list[i]

res = str_list[0] + stroka[::-1] + str_list[len(str_list) - 1]
print(res)