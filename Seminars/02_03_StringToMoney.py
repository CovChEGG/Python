# 3)Дана строка текста. Напишите программу для подсчета стоимости строки,
# исходя из того, что один любой символ (в том числе пробел) стоит 60 копеек.
# Ответ дайте в рублях и копейках.
def price_of_string(my_sting):
    kop = len(my_sting) * 60
    rub = kop // 100
    kop -= rub * 100
    return '{0} руб {1} коп'.format(str(rub), str(kop))


input_str = input('Введите строку: ')
print(price_of_string(input_str))
