"""
Input: a string of parentheses from left to right
Return: true if they are balanced, false if not

* balanced parentheses:
- Each opening symbol has a corresponding closing symbol
- The pairs of parentheses are properly nested

Observation:
- Most recent opening parenthesis must match the next closing symbol
- The first opening symbol processed may have to wait until the very last symbol for its match
"""
from stack.stack import Stack


def is_balanced_parentheses(string: str):
    stack = Stack()
    for char in string:
        if char == "(":
            stack.push("(")
        elif char == ")":
            if stack.isempty():
                return False
            else:
                stack.pop()

    if stack.isempty():
        return True
    else:
        return False
