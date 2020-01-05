"""
Infix: the operator is in between the two operands that it is working on.
Each operator has a **precedent** level.
Operators of higher precedence are used before operators of lower precedence.
- Precedence of * and / > precedence of + and -.
- If equal precedence, left-to-right ordering or associativity is used.
- Add parentheses to change the order.

Fully parenthesized:
- To guarantee no confusion with respect to the order of operations.
- Use one pair of parentheses for each operator.
- The parentheses dictate the order of operations.
- No ambiguity, no need to remember any precedence rules.

i.e.
- A + B * C + D = ((A + (B * C)) + D) # multiplication > plus
- A + B + C + D = (((A + B) + C) + D) # left to right

Prefix: All operators precede the two operands that they work on
Postfix: All operators come after the operands that they work on i.e. AB -
i.e.
|Infix                  | Prefix            | Postfix       |
| --------------------- | ----------------- | ------------- |
| A + B                 | + A B             | A B +         |
| A + B * C             | + A * B C         | A B C * +     |
| ( A + B ) * C         | * + A B C         | A B + C *     |
| A + B * C + D         | + + A * B C D     | A B C * + D + |
| ( A + B ) * ( C + D ) | * + A B + C D     | A B + C D + * |
| A * B + C * D         | + * A B * C D     | A B * C D * + |
| A + B + C + D         | + + + + + A B C D | A B + C + D + |

Problem:
Input: A string of tokens delimited by spaces. Operator tokens are *, /, +, -, (, ). Operand tokens are
single-character identifiers A, B, C,...

Algorithm:
- Fully parenthesize the expression using the order of operations.
- Move the enclosed operator to the position of either the left (prefix) or the right parenthesis (postfix).

- Create an empty stack for keeping operators. Create an empty list for output.
- Convert the input infix string to a list by using the string method.
- Scan the token list from left to right.
- If the token is an operand, append it to the end of the output list.
- If the token is a left parenthesis, push it on the stack.
- If the token is a right parenthesis, pop the stack until the corresponding left parenthesis is removed.
  Append each operator to the end of the output list.
- If the token is an operator other than parenthesis, move any operators on the stack with a higher or equal precedence and
  append them to the output list, and push it on the stack.
"""
import re

from stack import Stack


def ge_precedence(a: str, b: str) -> bool:
    precedences = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2, "**": 3}
    return precedences[a] >= precedences[b]


def infix_str_to_list(infix: str) -> list:
    """
    Convert an infix str to list (Does not consider negative number)
    Look for either int or float or any character which isn't digit or a space
    """
    if re.search("[^ 0-9.()+\-*/]", infix):
        raise SyntaxError("invalid syntax")
    number_or_symbol = re.compile("(\d*\.\d+|\d+|[()]|[^ 0-9()]+)")
    return re.findall(number_or_symbol, infix)


def infix_to_postfix(infix: str) -> str:
    """
    Use a stack to keep the operators. The top of the stack will always be the most recently saved operator.
    When reading the new operator, compare the precedence of the added one and the recently saved one
    """
    operator_stack = Stack()
    postfix_list = []
    tokens = infix_str_to_list(infix)
    for token in tokens:
        if token not in "+-*/()**":
            postfix_list.append(token)
        elif token == "(":
            operator_stack.push(token)
        elif token == ")":
            while True:
                operator = operator_stack.pop()
                if operator == "(":
                    break
                else:
                    postfix_list.append(operator)
        elif token in "+-*/**":
            while True:
                if operator_stack.isempty():
                    break
                if ge_precedence(operator_stack.peek(), token):
                    operator = operator_stack.pop()
                    postfix_list.append(operator)
                else:
                    break
            operator_stack.push(token)

    while not operator_stack.isempty():
        operator = operator_stack.pop()
        postfix_list.append(operator)
    return " ".join(postfix_list)


def eval_postfix(postfix_str: str) -> float:
    """
    Whenever an operator is seen on the input, the two most recent operands will be used in the evaluation.
    :param postfix_str:
    :return:
    """
    operand_stack = Stack()
    tokens_list = postfix_str.split()

    for token in tokens_list:
        if token in "+-*/**":
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = calc(operand1, token, operand2)
            operand_stack.push(result)
        else:
            try:
                token = float(token)
            except ValueError:
                raise SyntaxError("invalid operand")
            operand_stack.push(token)
    return operand_stack.pop()


def calc(operand1: float, operator: str, operand2: float) -> float:
    """
    :return: the answer of the math formula `operand1 operator operand2`
    """
    formula_dict = {
        "*": operand1 * operand2,
        "/": operand1 / operand2,
        "-": operand1 - operand2,
        "+": operand1 + operand2,
        "**": operand1 ** operand2
    }
    try:
        return formula_dict[operator]
    except KeyError:
        raise SyntaxError("invalid operator")


if __name__ == "__main__":
    postfix = infix_to_postfix("5 * 3 ** ( 4 - 2 )")
    print(postfix)
    answer = eval_postfix(postfix)
    print(answer)
