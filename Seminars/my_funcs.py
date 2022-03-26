def int_input_n(txt, first_number=1):
    while True:
        in_string=input('Введите ' + txt + ': ')
        if in_string.isdigit() == 1:
            in_int = int(in_string)
            if in_int >= first_number:
                return in_int
        print('\n!!! Не корректный ввод натурального числа !!! Попробуйте ещё раз, пожалуйста.\n')