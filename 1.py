# Задание 1- вывести папки и файлы в корневой директории
import os

res_list = []

for dir, folders, files in os.walk("Work"):
    for direction in folders:
        res_list.append(f"{dir}//{direction}")
    for file in files:
        res_list.append(f"{dir}//{file}")
    break
print(res_list)
