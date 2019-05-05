def similarity(char1: str, char2: str)->int:
    """
    :param char1:
    :param char2:
    :return: the similarity score between char1 and char2. +3 if they are same, -3 if they are different.
    """
    if char1 == char2:
        return 3
    else:
        return -3


def local_alignment(str1: str, str2: str, gap_cost: int):
    """
    :param str1: a string longer than str2
    :param str2:
    :param gap_cost:
    :return:
    """
    # create a (n+1) * (m+1) matrix
    opt = [[None for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    # initialize its first row and first column to be 0
    for i in range(len(str1) + 1):
        opt[i][0] = 0
    for j in range(1, len(str2) + 1):
        opt[0][j] = 0

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # if align str1[i-1] and str2[j-1]
            opt1 = opt[i - 1][j - 1] + similarity(str1[i - 1], str2[j - 1])
            # if str1[i-1] is at the end of a gap of a gap of length k
            opt2 = opt[i - 1][j] - gap_cost
            # if str2[j-1] is at the end of a gap of length l
            opt3 = opt[i][j - 1] - gap_cost
            opt4 = 0
            opt[i][j] = max(opt1, opt2, opt3, opt4)
    for line in opt:
        print(line)
    return opt[-1][-1]
