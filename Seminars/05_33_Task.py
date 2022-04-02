# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = 3
any_list = [random.randint(0, 100) for i in range(k + 1)]
print(any_list)
many_num = ''
n = k
for i in range(k + 1):
    if n == 1:
        many_num += str(any_list[i]) + '*x + '
    elif n == 0:
        many_num += str(any_list[i]) + ' = 0'
    else:
        many_num += str(any_list[i]) + f'*x^{n} + '
    n -= 1
print(many_num)
data = open('05_33_Task_2.txt', 'a')
data.write(many_num + '\n')
data.close()

# '05_33_Task_2.txt'
# '05_34_In_2.txt'
