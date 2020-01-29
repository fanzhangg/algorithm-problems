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


def nest(coeefs: list, x: int or float, base_points: list)->int or float:
    """
    Evaluates polynomial from nested form using Horner’s Method
    :param coeefs: coefficients (constant term first)
    :param x: x-coordinate
    :param base_points: a list of base points
    :return: value of polynomial at x
    """
    y = coeefs[-1]
    for i in range(len(coeefs)-2, -1, -1):
        y = y * (x - base_points[i]) + coeefs[i]
    return y


nest([1, 1/2, 1/2, -1/2], 1, [0, 2, 3])
horner([13, 9, 2, 6, 3], 2, is_decr=False)
