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


N = int_input('целое число')
sum_N = 0
while N:
    sum_N += N % 10
    N = N // 10
print(sum_N)