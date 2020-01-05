"""
find factorial of 10 = find the factorial of 9 and multiply it by 10
find factorial of 9 = find the factorial of 8 and multiply it by 9
...
find the factorial of 1 - base case
"""


def factorial(n):
    """
    find the factorial of a number
    :param n:
    :return:
    """
    # base case: if the number is 1
    if n == 1:
        # factorial of 1 is 1, return 1
        # no actual answer is provided until the base case has been reached
        # function class are saved in the call items
        # once the base case has been found, the answer trickles back up the call items
        # until the final answer is reached
        print(n)
        return 1
    else:
        # if the number is greater than 1, multiply the number by the factorial of the next number down
        answer = n * factorial(n - 1)
        print("n:", n)
        print("answer:", answer)
        return answer


def get_sum(n):
    """
    find the sum from 1 to n
    :param n:
    :return:
    """
    if n == 1:
        return 1
    else:
        return n + get_sum(n - 1)


def find_gcd(n: int, m: int) -> int:
    """
    find the largest number than can divide into them
    :param n:int
    :param m: int (n > m by default)
    :return: the largest common divisor
    """
    reminder = n % m
    while reminder:
        if reminder:
            n = min(n, m)
            m = reminder
            reminder = n % m
            print("n:", n, "m:", m, "reminder:", reminder)
    return m


def find_gcd_2(n, m):
    if n % m == 0:
        return m
    else:
        return find_gcd_2(m, n % m)


def count_co_prime(n: int) -> list:
    """
    a, b are co-primes if their greatest common divisor is 1
    :param n: int
    :return: list of co-prime of n
    """
    co_primes = []
    for x in range(1, n):
        if find_gcd_2(n, x) == 1:
            co_primes.append(x)
    return co_primes


def find_palindrome(s: str) -> bool:
    """
    a palindrome is a word that reads the same forward as it does backward. (i.e. "hannah)
    :param s:
    :return:
    """
    if len(s) <= 1:
        return True
        # remove the first and last char of s if they are same
    elif s[0] == s[-1]:
        s = s[1:-1]
        return find_palindrome(s)
    else:
        return False


def fib(n: int) -> int:
    """
    Fibonacci sequence: starts with 1, 1 and then add the last number to the number preceding ti in the sequence
    :param n:
    :return:
    """
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)
