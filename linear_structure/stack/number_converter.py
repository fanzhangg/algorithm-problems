from stack import Stack


def dec_to_bin(num: int) -> str:
    """
    Convert integer values into binary numbers

    Algorithm: Divided By 2
    - Start with an integer greater than 0
    - Continuously divide the number by 2 and keep track of the reminder
    - the reversed string of reminders is the binary string

    i.e. The binary string of 233 is 11101001
    1 | 233
    0 | 116
    0 | 58
    1 | 29
    0 | 14
    1 | 7
    1 | 3
    1 | 1
        0
    """
    stack = Stack()
    while num != 0:
        reminder = num % 2
        stack.push(reminder)
        num = num // 2
    bin_str = ""
    while not stack.isempty():
        bin_digit = stack.pop()
        bin_str = "".join((bin_str, str(bin_digit)))
    return bin_str


def dec_to_hex(num: int) -> str:
    """
    Convert a decimal number to hexadecimal string
    :param num: a decimal number
    :return: a hexadecimal string (A for 10, B for 11, ...)
    """
    stack = Stack()
    hex_str = ""
    digits = "0123456789ABCDEF"

    while num != 0:
        reminder = num % 16
        stack.push(reminder)
        num = num // 16

    while not stack.isempty():
        digit = stack.pop()
        hex_str = "".join((hex_str, digits[digit]))
    return hex_str


def dec_to_oct(num: int) -> str:
    """
    Convert a decimal number to a octal string
    """
    stack = Stack()
    oct_str = ""

    while num != 0:
        reminder = num % 8
        stack.push(reminder)
        num = num // 8

    while not stack.isempty():
        digit = stack.pop()
        oct_str = "".join((oct_str, str(digit)))
    return oct_str


if __name__ == "__main__":
    print(dec_to_oct(25))
    print(dec_to_hex(256))
