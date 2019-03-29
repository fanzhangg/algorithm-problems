def count_down(n, step=-1):
    if step >= 0:
        raise ValueError("step >= 1")
    if n == 0:
        print(n)
    elif n < 0:
        return
    else:
        print(n)
        count_down(n+step, step)
