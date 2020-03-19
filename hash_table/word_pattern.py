def wordPattern(pattern, str):
    """
    Given a pattern and a string str, find if str follows the same pattern.
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    word_dict = {}
    token_dict = {}

    words = str.split()

    if not len(words) == len(pattern):
        return False

    for i in range(len(words)):
        word = words[i]
        token = pattern[i]

        print(word, token)

        if word in word_dict.keys() and not token == word_dict[word]:
            return False
        if token in token_dict.keys() and not word == token_dict[token]:
            return False
        word_dict[word] = token
        token_dict[token] = word
    return True


print(wordPattern("abba", "dog cat cat fish"))
