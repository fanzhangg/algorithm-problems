def compress_str(s: str)->str:
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1
    chars = list(counter.keys())
    chars.sort(key=str.lower)
    result = ""
    for char in chars:
        result = "".join((result, char, str(counter[char])))
    return result
