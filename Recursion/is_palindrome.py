def is_palindrome(word: str)->bool:
    """
    :return: true if a word is a palindrome
    """
    if len(word) < 2:
        return True
    elif not word[0] == word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])


def is_palindrome_2(word: str)->bool:
    return word == word[::-1]

