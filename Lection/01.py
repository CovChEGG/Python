# print('hello мир')
val = None
a = 1234
b = 1.23
print('\n')
print(type(a), '\t', '\t', a)
print(type(b), '\t', b)
print(type(val), '\t', val)
val = 21341232
print(type(val), val)
s = 'hello мир'
print(type(s), s, '\n')
print(a, '-', b, '-', s, '\n')
print(f'{a} - {b} - {s}', '\n')
print('{} - {} - {}'.format(a,b,s), '\n')
print('{1} - {2} - {0}'.format(a, b, s), '\n')
a = int(input('a= '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)