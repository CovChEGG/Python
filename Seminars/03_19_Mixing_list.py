# Реализовать алгоритм перемешивания списка.
from random import randint

import random

import my_funcs as mf

n = mf.int_input_n('натуральное число N', 0)
input_list = [i for i in range(-n, n + 1)]
shuffle_list = [i for i in range(-n, n + 1)]
random.shuffle(shuffle_list)
print(input_list)
print(shuffle_list)
output_list = []
tmp = len(input_list)-1
for i in range(len(input_list)):
    rnd = randint(0, tmp)
    output_list.append(input_list.pop(rnd))
    tmp -= 1
print(output_list)