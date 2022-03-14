# Найти расстояние между двумя точками пространства
def input_int(txt):
    while True:
        in_string = input('Введите координату точки ' + txt + ': ')
        if in_string.isdigit() == 1:
            return int(in_string)
        print('\n!!! Не корректный ввод!!! Попробуйте ещё, пожалуйста.\n')


x1 = input_int('x1')
y1 = input_int('y1')
z1 = input_int('z1')
x2 = input_int('x2')
y2 = input_int('y2')
z2 = input_int('z2')
distance = ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5
print(round(distance, 2))
