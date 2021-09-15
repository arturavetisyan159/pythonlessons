import re
mytext = 'Vasya aaaaaa 1972, Kolya - 107rw;   yandex'

"""
\d = any digit 0-9
\D = any non Digit
\w = any alphabet symbol
\W = any non alphabet
\s = any space
\S = any nonspace



"""


textlookfor = r"yandex"
allresults = re.findall(textlookfor, mytext)

print(allresults)
