# Сложите цифры целого числа.
def int_input(txt):
    while True:
        in_string = input('Введите ' + txt + ': ')
        if in_string.isdigit() == 1:
            in_int = int(in_string)
            if in_int >= 0:
                return in_int
            else:
                return -in_int
        print('\n!!! Не корректный ввод !!! Попробуйте ещё раз, пожалуйста.\n')


N = str(int_input('целое число'))
Sum_N = 0
for i in range(len(N)):
    Sum_N += int(N[i])
print(Sum_N)
