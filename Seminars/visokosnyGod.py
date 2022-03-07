# Натуральное число.
# Год високосный? Если его номер кратен 4, но не кратен 100, а также он кратен 400
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(True)
else:
    print(False)