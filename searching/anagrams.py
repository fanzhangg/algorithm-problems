def anagrams(str1: str, str2: str):
    """
    Decide if 2 string are anagrams, if one can be rearranged to be the other
    :param str1: str
    :param str2: str
    :return: bool
    """
    if not len(str1) == len(str2):
        return False
    for x in str1:
        if x in str2:
            j = str2.index(x)
            str2 = str2[:j] + str2[j+1:]
        else:
            return False
    return True
