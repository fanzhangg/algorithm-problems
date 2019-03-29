def reverse_str(string: str)->str:
    if len(string) == 0:
        return ""
    else:
        return reverse_str(string[1:]) + string[0]


def get_palindrome(string: str)-> str:
    return "".join((string, reverse_str(string)))
