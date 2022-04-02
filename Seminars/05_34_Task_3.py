# Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.


def read_ff(path):
    data = open(path, 'r')
    data_str = data.readline()
    data.close()
    return data_str


def str2dic(my_str):
    lst = list(map(str, my_str.strip().split(' ')))
    res = {}
    tmp_val = ''
    j = 0
    for i in lst:
        if i == '-' or i == '+':
            tmp_val = i
        elif '*' in i:
            j = i.find('*')
            res[i[j + 1:]] = int(tmp_val + i[:j])
            tmp_val = ''
        elif 'x' in i:
            res[i[0:]] = 1
        elif i.isdigit():
            res['0'] = int(tmp_val + i)
        elif '=' == i:
            return res


def sum_dics(dic1, dic2):
    all_keys = list(set(dic1.keys()) | set(dic2.keys()))
    all_keys.sort()
    res = dict()
    for i in all_keys:
        if i not in dic1.keys():
            res[i] = dic2[i]
        elif i not in dic2.keys():
            res[i] = dic1[i]
        else:
            res[i] = int(dic1[i]) + int(dic2[i])
            if res[i] == 0:
                del res[i]
    return res


def convert_dic(dic):
    all_keys = list(dic.keys())
    all_keys.sort()
    ak_len = len(all_keys)
    if '0' in all_keys:
        if dic['0'] < 0:
            dic['0'] = ' - ' + str(-dic['0'])
        else:
            dic['0'] = ' + ' + str(dic['0'])
    for i in range(1, ak_len):
        if dic[all_keys[i]] < 0:
            if -dic[all_keys[i]] != 1:
                dic[all_keys[i]] = ' - ' + str(-dic[all_keys[i]]) + '*'
            else:
                dic[all_keys[i]] = ' - '
        elif i == ak_len - 1:
            if dic[all_keys[i]] != 1:
                dic[all_keys[i]] = str(dic[all_keys[i]]) + '*'
            else:
                dic[all_keys[i]] = ''
        else:
            if dic[all_keys[i]] != 1:
                dic[all_keys[i]] = ' + ' + str(dic[all_keys[i]]) + '*'
            else:
                dic[all_keys[i]] = ' + '
    return dic


def res_string(dic):
    res_str = ' = 0'
    if '0' in dic.keys():
        res_str = dic.pop('0') + res_str
    for item in dic.keys():
        res_str = dic[item] + item + res_str
    return res_str


dic1 = str2dic(read_ff('05_34_In_1.txt'))
dic2 = str2dic(read_ff('05_34_In_2.txt'))
print('\n', dic1, '\n', dic2)
dic_sum = sum_dics(dic1, dic2)
resut_string = res_string(convert_dic(dic_sum))
print(resut_string)
data = open('05_34_out.txt', 'w')
data.writelines(resut_string)
data.close()
