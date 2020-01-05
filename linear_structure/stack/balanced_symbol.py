"""
Given: A string of mixed symbols
Output: True if each maintains its own opeen and close relationships; False if not
"""
from stack.stack import Stack


def is_balanced_symbols(string: str):
    stack = Stack()
    for char in string:
        if char in "([{":
            stack.push(char)
        elif char in "}])":
            if stack.isempty():
                return False
            elif match(stack.peek(), char):
                stack.pop()
            else:
                return False
    if stack.isempty():
        return True
    else:
        return False


def match(opener: str, closer: str) -> bool:
    openers = "([{"
    closers = ")]}"
    return openers.index(opener) == closers.index(closer)


s = "[[]]()"
print(is_balanced_symbols(s))
