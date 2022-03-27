# 2)Написать калькулятор с операциями:
# Умножение, деление, остаток от деления,
# вычитание, целочисленное деление.
def calc(a, b, action):
    if action == '+':
        return a + b
    elif action == '-':
        return a - b
    elif action == '*':
        return a * b
    elif b == 0:
        print('Деление на 0 не допустимо!!!')
        return 0
    else:
        if action == '/':
            return a / b
        elif action == '%':
            return a % b
        elif action == '//':
            return a // b


def int_input(txt):
    while True:
        in_string = input('Введите ' + txt + ': ').strip()
        negative_or_positive = 1
        if in_string[0] == '-':
            in_string = in_string[1:]
            negative_or_positive = -1
        if in_string.isdigit() == 1:
            return negative_or_positive * int(in_string)
        print('\n!!! Не корректный ввод !!! Попробуйте ещё раз, пожалуйста.\n')


x = int_input('первый элемент')
y = int_input('второй элемент')
while True:
    sign = input("Введите операцию: ")
    if sign in ['+', '-', '*', '/', '//', '%']:
        print(calc(x, y, sign))
        break
    else:
        print('Не допустимое действие, попробуйте ещё!')
