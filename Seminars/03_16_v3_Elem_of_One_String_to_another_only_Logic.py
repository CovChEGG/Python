# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
def calc_occurrences(text, pattern):
    i = 0
    j = 0
    counter = 0
    while i < len(text):
        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                counter += 1
                j = 0
            else:
                j += 1
        i += 1
    return counter


string_one = input("Введите первую строку: ")
string_two = input("Введите вторую строку: ")
calc = 0
if string_one == string_two:
    print("Строки идентичны, ", end="")
    calc = 1
elif string_two in string_one:
    calc = calc_occurrences(string_one, string_two)
    if calc:
        print("Вторая строка входит в первую, ", end="")
elif string_one in string_two:
    calc = calc_occurrences(string_two, string_one)
    if calc:
        print("Первая строка входит во вторую, ", end="")
if calc == 0:
    print("Нет вхождений одной строки в другую, ", end="")
print(f"количество вхождений равно: {calc}")
