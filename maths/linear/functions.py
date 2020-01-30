import numpy


def horner(coeffs: [int or float], x: int or float, is_decr=True)->int:
    """
    This function evaluate a polynomial via Horner's method
    :param coeffs:
    :param x:
    :param is_decr:
    :return:
    """
    if is_decr:
        ans = coeffs[0]
        for i in range(1, len(coeffs)):
            ans = ans * x + coeffs[i]
    else:
        ans = coeffs[-1]
        for i in range(len(coeffs) - 2, -1, -1):
            ans = ans * x + coeffs[i]
    return ans


def nest(coeffs: list, x: int or float, base_points: list)-> int or float:
    """
    Evaluates polynomial from nested form using Horner’s Method
    :param coeffs: coefficients (constant term first)
    :param x: x-coordinate
    :param base_points: a list of base points
    :return: value of polynomial at x
    """
    y = coeffs[-1]
    for i in range(len(coeffs) - 2, -1, -1):
        y = y * (x - base_points[i]) + coeffs[i]
    return y


def int_dec_to_bin(num: int)->str:
    """
    :param num: an integer
    :return: the binary number of num
    """
    bins = []
    while True:
        bins.insert(0, str(num % 2))
        num = num // 2

        if num == 0:
            return "".join(bins)


def frac_dec_to_bin(frac: float, accurates: int)->str:
    """
    :param frac: the fraction of a float
    :param accurates: the accuracies of the binary number
    :return: a binary number of a fraction
    """
    bins = []
    if frac >= 1 or frac < 0:
        raise ValueError("frac must be a fraction")

    for _ in range(accurates):
        frac = frac * 2
        frac_int = int(frac // 1)
        frac = frac % 1

        bins.append(str(frac_int))
        frac = frac
    return "".join(bins)


def float_dec_to_bin(fl: float, accurates: int)->str:
    """
    :param fl: a float number
    :param accurates: the accuracies of the binary number
    :return: the binary number of the float
    """
    int_str = int_dec_to_bin(int(fl))
    frac_str = frac_dec_to_bin(fl % 1, accurates)
    return ".".join((int_str, frac_str))


def int_bin_to_dec(bin_str: str):
    """
    :param bin_str: a binary integer
    :return: the decimal integer
    """
    ans = 0
    for i in range(len(bin_str)):
        x = int(bin_str[i])
        p = len(bin_str) - 1 - i
        ans += x * (2 ^ p)
    return ans


def frac_bin_to_dec(bin_str: str):
    ans = 0
    for i in range(len(bin_str)):
        x = int(bin_str[i])
        p = len(bin_str) - i
        ans += x * 1 / (2 ^ p)
    return ans


nest([1, 1/2, 1/2, -1/2], 1, [0, 2, 3])
horner([13, 9, 2, 6, 3], 2, is_decr=False)
