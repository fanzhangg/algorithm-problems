from ds.stack import ArrayStack


def is_balanced_symbols(string: str):
    """
    :param string: A string of mixed symbols
    :return True if each bracket maintains its own open and close relationships; False if not
    """
    stack = ArrayStack()
    for char in string:
        if char in "([{":
            stack.push(char)
        elif char in "}])":
            if stack.is_empty():
                return False
            elif match(stack.top(), char):
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


def match(opener: str, closer: str) -> bool:
    """
    :param opener: a character in "([{"
    :param closer: a character in ")]}"
    :return: True if the opener matches the closer
    """
    openers = "([{"
    closers = ")]}"
    return openers.index(opener) == closers.index(closer)


s = "[[]]()"
print(is_balanced_symbols(s))
