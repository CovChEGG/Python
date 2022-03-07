# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат
X = [False, True]
Y = [False, True]
Z = [False, True]
for i in X:
    for j in Y:
        for k in Z:
            if not(X[i] or Y[j] or Z[k]) == (not X[i] and not Y[j] and not Z[k]):
                print(True)
            else:
                print(False)

