def sum_range(start, stop, step=1):
    if start > stop:
        return 0
    elif start == stop:
        return stop
    else:
        return start + sum_range(start + step, stop, step)


