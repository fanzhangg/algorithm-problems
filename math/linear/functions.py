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


ans = nest([1, 1/2, 1/2, -1/2], 1, [0, 2, 3])
print(ans)
