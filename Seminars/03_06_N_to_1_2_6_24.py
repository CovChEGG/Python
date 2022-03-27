# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
import my_funcs as mf
N = mf.int_input_n('число N')
list_n = [1]
for i in range(1, N):
    list_n.append(list_n[i-1]*(i+1))
print(list_n)
