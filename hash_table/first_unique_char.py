from collections import Counter

def find_first_unique_char(s: str):
    """
    return: the index of the first non-repeating character in it; return -1 if it does not exist
    """
    chars = {}
        
    for char in s:
        chars[char] = chars.get(char, 0) + 1

    index = 0  

    for idx, ch in enumerate(s):
        if chars[ch] == 1:
            return idx     
    return -1

if __name__ == "__main__":
    # print(find_first_unique_char(""))
    print(find_first_unique_char("aabb"))
    print(find_first_unique_char("baabcddeeeeaa"))
