# 08. Сообщить в какой четверти координатной плоскости
# или на какой оси находится точка с координатами Х и У
def int_input(txt):
    while True:
        in_string=input('Введите ' + txt + ': ')
        if in_string.isdigit() == 1:
            return int(in_string)
        print('\n!!! Не корректный ввод!!! Попробуйте ещё, пожалуйста.\n')


quarter = int_input("номер четверти")
if quarter == 1:
    print("X > 0 and Y > 0")
elif quarter == 2:
    print("X < 0 and Y > 0")
elif quarter == 3:
    print("X < 0 and Y < 0")
elif quarter == 4:
    print("X > 0 and Y < 0")
else:
    print("Такой четверти нет!")
    