# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
def int_input(txt):
    while True:
        in_string=input('Введите '+ txt + ': ')
        if in_string.isdigit() == 1:
            return int(in_string)
        print('\n!!! Не корректный ввод!!! Попробуйте ещё, пожалуйста.\n')


N = int_input("n")
if N == 0:
    print('Некорректный ввод натурального числа!!!')
else:
    slovar = {x: 3*x+1 for x in range(1, N+1)}
    print(slovar)
