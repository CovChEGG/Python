# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
def int_input(txt):
    while True:
        in_string = input('Введите ' + txt + ': ')
        if in_string.isdigit() == 1:
            in_int = int(in_string)
            if in_int >= 0:
                return in_int
        print('\n!!! Не корректный ввод !!! Попробуйте ещё раз, пожалуйста.\n')


N = int_input('n')
tmp = 1
my_list = [tmp]
for i in range(N - 1):
    tmp *= -3
    my_list.append(tmp)
print(my_list)
