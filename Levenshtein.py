import numpy as np


def edit_distance_Levenshtein(source, target):
    n = len(source)
    m = len(target)
    D = np.zeros((n + 1, m + 1))

    for row in range(1, n + 1):
        D[row][0] = D[row - 1][0] + 1

    for column in range(1, m + 1):
        D[0][column] = D[0][column - 1] + 1

    for row in range(1, n + 1):
        for column in range(1, m + 1):
            if source[row - 1] != target[column - 1]:
                subs = 2
            else:
                subs = 0
            D[row][column] = min(D[row - 1][column] + 1, D[row][column - 1] + 1, D[row - 1][column - 1] + subs)

    print(D)
    return D[n][m]


res = edit_distance_Levenshtein("intention", "execution")
print(res)
