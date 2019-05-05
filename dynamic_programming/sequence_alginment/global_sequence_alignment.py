def alignment(str1: str, str2: str, gap_cost: int, mismatch_costs: dict)->tuple:
    """
    :param str1:
    :param str2:
    :param gap_cost: penalty for skipping a space
    :param mismatch_costs: mismatch cost for each pair of letter in alphabet
    :return: the minimal total cost
    """
    opt = [[None for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        opt[i][0] = i * gap_cost
    for j in range(len(str2) + 1):
        opt[0][j] = j * gap_cost

    str1_align = []
    str2_align = []

    def get_string_queues(i, j):
        if j == 0 and i == 0:
            pass
        if j == 0:
            # insert reset str1 before the str1_align
            str1_align.insert(0, str1[:i])
            # insert i "-" before the str2_align
            str2_align.insert(0, "-" * i)
        elif i == 0:
            str2_align.insert(0, str2[:j])
            str1_align.insert(0, "-" * j)
        else:
            l_i = str1[i - 1]
            l_j = str2[j - 1]
            min_opt = min(mismatch_costs[l_i, l_j] + opt[i-1][j-1],
                          gap_cost + opt[i-1][j],
                          gap_cost + opt[i][j-1])
            if gap_cost + opt[i-1][j] == min_opt:
                str2_align.insert(0, "-")
                str1_align.insert(0, l_i)
                get_string_queues(i-1, j)
            elif gap_cost + opt[i][j-1] == min_opt:
                str1_align.insert(0, "-")
                str2_align.insert(0, l_j)
                get_string_queues(i, j-1)
            else:
                str1_align.insert(0, l_i)
                str2_align.insert(0, l_j)
                get_string_queues(i-1, j-1)

    def list_to_str(li: list)->str:
        return "".join(li)

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            l_i = str1[i - 1]
            l_j = str2[j - 1]
            opt[i][j] = min(mismatch_costs[l_i, l_j] + opt[i-1][j-1],
                            gap_cost + opt[i-1][j],
                            gap_cost + opt[i][j-1])
    get_string_queues(len(str1), len(str2))
    str1_align = list_to_str(str1_align)
    str2_align = list_to_str(str2_align)
    return opt[-1][-1], str1_align, str2_align
