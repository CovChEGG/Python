# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import my_funcs as mf
n = mf.int_input_n('число членов последовательности N', 0)
result = [(-3)**x for x in range(n)]
print(result)
