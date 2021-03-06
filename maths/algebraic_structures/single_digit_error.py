def has_single_digit_error(number: str):
    """
    number: a universal product code
    :return: true if the code has a single-digit error, code % 9 !== 0, else false
    """
    num_li = [int(i) for i in number]
    dot_product = 0
    mult = 3
    for n in num_li:
        dot_product += mult * n
        if mult == 3:
            mult = 1
        else:
            mult = 3
    print(dot_product)
    if dot_product % 10 == 0:
        return False
    else:
        return True


ans = has_single_digit_error("021000658978")
print(ans)
