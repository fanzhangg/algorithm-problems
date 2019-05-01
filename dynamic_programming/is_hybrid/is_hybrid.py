def is_hybrid(x: str, y: str, z: str)->bool:
    """
    :optimal substructure:
    - If i = 0, j = 0, opt[0, 0] = True
    - If i = 0, opt[0, j] = opt[0, j-1]  and y[j] = z[j]
    - If j = 0, opt[i, 0] = opt[i-1, 0] and x[i-1] = z[i]
    - opt[i, j] = (opt[i-1, j] and x[i] = z[i + j]) or (opt[i, j-1] + y[j] = z[i+j])
    :param x: a str of p
    :param y: a str of q
    :param z: a str of m
    :return: true if x is a hybrid of y and z
    """
    if not len(x) + len(y) == len(z):
        return False

    opt = [[None for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    opt[0][0] = True

    for i in range(1, len(x) + 1):
        if opt[i - 1][0] and x[i - 1] == z[i - 1]:
            opt[i][0] = True
        else:
            opt[i][0] = False

    for j in range(1, len(y) + 1):
        if opt[0][j - 1] and y[j - 1] == z[j - 1]:
            opt[0][j] = True
        else:
            opt[0][j] = False

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if opt[i][j-1] and y[j - 1] == z[i + j - 1]:
                opt[i][j] = True
            elif opt[i-1][j] and x[i - 1] == z[j + i - 1]:
                opt[i][j] = True
            else:
                opt[i][j] = False

    return opt[-1][-1]
