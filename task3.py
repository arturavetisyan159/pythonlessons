with open('task3.txt', 'r', encoding='utf-8') as fr:
    lines = fr.readlines()
    print(f'В файле {len(lines)} строки')
    counter = 1
    total_amount_symb = 0
    for i in range(0, len(lines)):
        if '\n' in lines[i]:
            lines[i] = lines[i].replace('\n', '')
    for line in lines:
        for s in line:
            total_amount_symb += 1
        print(f'В {counter} строке {total_amount_symb} символов, {len(line.split())} слов!')
        total_amount_symb = 0
        counter += 1

