# При заданном целом числе n посчитайте n + nn + nnn.
def int_input(txt):
    while True:
        in_string = input('Введите ' + txt + ': ')
        if in_string.isdigit() == 1:
            in_int = int(in_string)
            if in_int >= 0:
                return in_int
        print('\n!!! Не корректный ввод !!! Попробуйте ещё раз, пожалуйста.\n')


N = int_input('число n')
NN = int(str(N) * 2)
NNN = int(str(N) * 3)
print(f'{N} + {NN} + {NNN} = {N + NN + NNN}')
