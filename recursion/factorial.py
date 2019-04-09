def factorial(n):
    if n < 0:
        raise ValueError("n is less than 0")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
