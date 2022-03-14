# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
def int_input(txt):
    while True:
        in_string = input('Введите ' + txt + ': ')
        if in_string.isdigit() == 1:
            in_int = int(in_string)
            if in_int > 0:
                return in_int
        print('\n!!! Не корректный ввод !!! Попробуйте ещё раз, пожалуйста.\n')


S = int_input('количество секунд')
time_format = "{0}:{1}:{2}:{3}".format(S // 86400,
                                       (S % 86400) // 3600,
                                       ((S % 86400) % 3600) // 60,
                                       ((S % 86400) % 1440) % 60
                                       )
print(time_format)
