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
    :param gap_cost: a negative int
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
            match = opt[i - 1][j - 1] + similarity(str1[i - 1], str2[j - 1])
            # if str1[i-1] is at the end of a gap of a gap of length k
            delete = opt[i - 1][j] + gap_cost
            # if str2[j-1] is at the end of a gap of length l
            insert = opt[i][j - 1] + gap_cost
            opt[i][j] = max(match, delete, insert, 0)


    def get_optimal_score():
        """
        :return: the score of the optimal solution such as the highest score in the matrix
        """
        max_score = 0
        curr_i = 0
        curr_j = 0
        for i in range(len(str1) + 1):
            for j in range(len(str2) + 1):
                if opt[i][j] > max_score:
                    max_score = opt[i][j]
                    curr_i, curr_j = i, j
        return max_score, curr_i, curr_j

    align_1_list = []
    align_2_list = []

    def trace_back(i, j):
        # if i == j == 1:
        #     # convert the list to str
        #     pass
        # else:
        char1 = str1[i - 1]
        char2 = str2[j - 1]

        # if align str1[i-1] and str2[j-1]
        match = opt[i - 1][j - 1] + similarity(str1[i - 1], str2[j - 1])
        # if str1[i-1] is at the end of a gap of a gap of length k
        delete = opt[i - 1][j] + gap_cost
        # if str2[j-1] is at the end of a gap of length l
        insert = opt[i][j - 1] + gap_cost
        opt4 = 0
        max_opt = max(match, delete, insert, opt4)

        if match == max_opt:
            # insert both letters to the string
            align_1_list.insert(0, char1)
            align_2_list.insert(0, char2)
            trace_back(i-1, j-1)
        elif delete == max_opt:
            align_1_list.insert(0, char1)
            align_2_list.insert(0, "-")
            trace_back(i-1, j)
        elif insert == max_opt:
            align_1_list.insert(0, "-")
            align_2_list.insert(0, char2)
            trace_back(i, j-1)
        elif max_opt == 0:
            pass

    optimal_score, opt_i, opt_j = get_optimal_score()
    trace_back(opt_i, opt_j)

    optimal_aligns = "".join(align_1_list), "".join(align_2_list)

    return optimal_score, optimal_aligns
