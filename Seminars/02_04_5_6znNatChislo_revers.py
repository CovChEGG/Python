# Дано пятизначное или шестизначное натуральное число.
# Напишите программу, которая изменит порядок его последних пяти цифр на обратный.
def reverse5last(num):
    if int(num) < 9999:
        print("Too small number! You need five or more")
        return num
    str_num = str(num)
    new_str = str_num[:-5]
    for i in range(0, 5):
        new_str = new_str + str_num[len(str_num) - 1 - i]
    return int(new_str)


a = 1234523
print(a)
print(reverse5last(a))
