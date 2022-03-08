# 08. Сообщить в какой четверти координатной плоскости
# или на какой оси находится точка с координатами Х и У
def input_int(txt):
    while True:
        in_string=input('Введите '+ txt + ': ')
        if in_string.isdigit() == 1:
            return int(in_string)
        print('\n!!! Не корректный ввод!!! Попробуйте ещё, пожалуйста.\n')

X = input_int("X")
Y = input_int("Y")
print(X,Y)
if X == 0 and Y == 0:
    print("Точка находится в начале координат")
elif X == 0:
    print("Точка лежит на оси Y")
elif Y == 0:
    print("Точка лежит на оси X")
elif X > 0 and Y > 0:
    print("Точка находится в первой четверти")
elif X < 0 and Y > 0:
    print("Точка находится во второй четверти")
elif X < 0 and Y < 0:
    print("Точка находится в третьей четверти")
else:
    print("Точка находится во второй четверти")
