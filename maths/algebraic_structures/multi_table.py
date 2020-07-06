def get_multi_table(nums: list, div: int)->str:
    """
    :param nums: a list of numbers
    :param div: the divisor
    :return: a markdown format multiplication table of *nums* using multiplication mode *div*
    """
    table = []
    for x in nums:
        row = []
        for y in nums:
            remain = x * y % div
            row.append(remain)
        table.append(row)

    s = "| "
    s += "mod" + str(div) + " | "
    s += " | ".join([str(n) for n in nums])
    s += " |\n"
    s += "| "
    s += " | ".join("--" for _ in range(len(nums) + 1))
    s += " |\n"

    for i in range(len(table)):
        row_str = str(nums[i]) + " | " + " | ".join([str(n) for n in table[i]])
        s += "| " + row_str + " |\n"
    return s


t = get_multi_table([1, 5, 7, 11], 12)
print(t)
