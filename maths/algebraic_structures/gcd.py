def gcd(a: int, b: int):
    """
    :param a: int
    :param b: int
    :return: Greatest common divisor
    """
    while not b == 0:
        t = b
        b = a % b
        a = t
    return a


def extended_gcd(a: int, b: int):
    """
    :param a: int
    :param b: int
    :return: a dictionary of the greatest common divisor, coefficients of Bezout's identity,
    and quotients
    """
    s = 0
    old_s = 1

    t = 1
    old_t = 0

    r = b
    old_r = a

    while not r == 0:
        quot = old_r // r
        old_r, r = r, old_r - quot * r
        old_s, s = s, old_s - quot * s
        old_t, t = t, old_t - quot * t

    return {
        "quotients": (t, s),
        "Bézout coefficients:": (old_s, old_t),
        "greatest common divisor": old_r
    }


ans = extended_gcd(38, 55)
print(ans)
