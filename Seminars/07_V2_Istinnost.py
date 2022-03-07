# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат
from turtle import clear


X = [False, True]
Y = [False, True]
Z = [False, True]
for i in X:
    for j in Y:
        for k in Z:
            left_part = not(X or Y or Z)
            right_part = (not X and not Y and not Z)
            result = left_part == right_part
            # # --bool type--
            # print('\t', left_part, '\t\t==\t', right_part, '\t\t\t = ', result)
            # print("¬({0} ⋁ {1} ⋁ {2})\t== ¬{0} ⋀ ¬{1} ⋀ ¬{2}\t Is {3}".format(
            #     X[i], Y[j], Z[k], result), '\n')
            # # --int type--
            print('      ', int(left_part), '\t==\t ', int(right_part), '\t\t = ', int(result))
            print('¬({0} ⋁ {1} ⋁ {2})\t==   ¬{0} ⋀ ¬{1} ⋀ ¬{2}\t Is {3}'.format(
                int(X[i]), int(Y[j]), int(Z[k]), int(result)), '\n')
