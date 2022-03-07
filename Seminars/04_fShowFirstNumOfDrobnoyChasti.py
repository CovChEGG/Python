# a = float(input("Введите число: "))
# str_a = str(a)
# count = 0
# for i in str_a:
#     count +=1
#     if i == '.':
#         print(str_a[count])

a = float(input("Введите число: "))
count = (a * 10) % 10 
print(int(count)) # откидываем не нужную дробную часть

