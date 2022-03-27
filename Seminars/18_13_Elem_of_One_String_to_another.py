# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
string_one = input("Введите первую строку: ")
string_two = input("Введите вторую строку: ")
count_in_one = string_one.count(string_two)
count_in_two = string_two.count(string_one)
if count_in_one == count_in_two != 0:
    print("Строки идентичны, количество вхождений равно: 1")
elif count_in_one:
    print(f"Количество вхождений второй строки в первую равно: {count_in_one}")
elif count_in_two:
    print(f"Количество вхождений первой строки во вторую равно: {count_in_two}")
else:
    print("Нет вхождений одной строки в другую! Количество вхождений равно: 0")
