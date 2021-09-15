# Задание 1. Является ли число римским?

import re
def is_roman(number):
    reg = re.compile(r"""
    ^M{0,3}
    (CM|CD|D?C{0,3})?
    (XC|XL|L?X{0,3})?
    (IX|IV|V?I{0,3})?$""", re.VERBOSE)
    if re.match(reg, number):
        return True
    else:    
        return False

print(is_roman('MMDCCLXXIII')) # True
print(is_roman('CCCMMVIIVV')) # False
