def int_input(txt):
    while True:
        in_string = input('Введите ' + txt + ': ')
        if in_string.isdigit() == 1:
            in_int = int(in_string)
            if in_int > 0:
                return in_int
        print('\n!!! Не корректный ввод !!! Попробуйте ещё раз, пожалуйста.\n')