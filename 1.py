# Задание 1: изменить букву в строке

def change_letters(stroka, s1, s2):
    res = ''
    for el in stroka:
        if el != s1:
            res += el
        else:
            res = res + s2
    return res


my_str = 'Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования.'

my_str = change_letters(my_str, 'N', 'P')
print(my_str)
