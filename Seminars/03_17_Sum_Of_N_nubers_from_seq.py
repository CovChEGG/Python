# Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму
# формула эйлера?
import my_funcs as mf

N = mf.int_input_n("число N (где N > 0)")
sum: float = 0
tmp: float = 0
# sum2: float = 0
# tmp2: float = 0
for i in range(1, N):
    tmp = tmp + (1 + 1 / N) ** N
    sum += tmp
    # tmp2 =  tmp2 + (i**(1/2.718281828))*2.718281828
    sum2 += tmp2
print(round(sum, 3))
# print(round(sum2, 3))

