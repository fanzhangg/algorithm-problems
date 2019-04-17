def recur_fib(n: int)->int:
    if n <= 1:
        return n
    else:
        return recur_fib(n - 1) + recur_fib(n - 2)


def memoized_fib(n: int)->int:
    fib_nums = [None for _ in range(n + 1)]

    def memoized_internal(n: int)->int:
        if fib_nums[n] is None:
            if n <= 1:
                fib_nums[n] = n
            else:
                fib_nums[n] = memoized_internal(n-2) + memoized_internal(n-1)
        return fib_nums[n]
    return memoized_internal(n)


def dynamic_fib(n: int)->int:
    fib_nums = [None for _ in range(n + 1)]
    fib_nums[0] = 0
    fib_nums[1] = 1
    for i in range(2, n+1):
        fib_nums[i] = fib_nums[i-1] + fib_nums[i-2]
    return fib_nums[n]

