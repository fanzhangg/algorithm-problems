def permute(s1: str, s2: str):
    """
        return: true if the 2 strings are permutable, false otherwise. 
        2 strings are permutable if each string is a permutation of the other (the same data, just possibly in a different ordering)
    """
    l2: list[str] = [x for x in s2]
    for c1 in s1:
        has_match = False
        for c2 in l2:
            if c1 == c2:
                has_match = True
                l2.remove(c2)  # remove the character from the list
                break
        if not has_match:
            return False
    if l2:  # l2 is empty
        return False
    else:
        return True
