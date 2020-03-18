def findWords(words):
        """
        Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = {"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
                "q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
        
        row2 = {"A", "S", "D", "F", "G", "H", "J", "K", "L",
                "a", "s", "d", "f", "g", "h", "j", "k", "l"}
        
        row3 = {"z", "x", "c", "v", "b", "n", "m",
                "Z", "X", "C", "V", "B", "N", "M"}
        
        output = []
            
        for word in words:
            valid = True
            
            # Determine which row the word supposed to be in
            char = word[0]
            if char in row1:
                row = row1
            elif char in row2:
                row = row2
            elif char in row3:
                row = row3
        
            for char in word:
                if char not in row:
                    valid = False
                    break
                    
            if valid:
                output.append(word)
        return output
                

input = ["Hello","Alaska","Dad","Peace"]
print(findWords(input))
