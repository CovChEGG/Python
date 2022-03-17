# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
def calc_occurrences(text, pattern, index=0, counter=0):
    new_index = text.find(pattern, index)
    if new_index >= 0:
        return calc_occurrences(text, pattern, new_index + 1, counter + 1)
    else:
        return counter


string_one = input("Введите первую строку: ")
string_two = input("Введите вторую строку: ")
if len(string_one) is len(string_two):
    print("Строки идентичны, ", end="")
    calc = 1
elif len(string_two) < len(string_one):
    print("Вторая строка входит в первую, ", end="")
    calc = calc_occurrences(string_one, string_two)
elif string_one in string_two:
    print("Первая строка входит во вторую, ", end="")
    calc = calc_occurrences(string_two, string_one)
else:
    print("Нет вхождений одной строки в другую, ", end="")
    calc = 0
print(f"количество вхождений равно: {calc}")
