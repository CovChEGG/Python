# Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt(по желанию) в одной строке одно число

import my_funcs as mf

n = mf.int_input_n('натуральное число N', 0)
new_list = [i for i in range(-n, n + 1)]
print(new_list)
path = '03_18_file.txt'
data = open(path, 'r')
summa = 0
print(f'\nИндексы из файла "{path}":')
for line in data:
    str_line = line.strip()
    if str_line.isdigit():
        int_line = int(line)
        if 0 <= int_line <= 2 * n:
            print(int_line)
            summa += new_list[int_line]
        else:
            print(f'{int_line} - Пропуск! Индекс выходит за пределы списка')
    else:
        print(f'{str_line} - Пропуск! Этот элемент строки не может быть индексом!')
print(f'\nСумма элементов с указанными индексами: {summa} ')
data.close()
