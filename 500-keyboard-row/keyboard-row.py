class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rowOne = set("qwertyuiop")
        rowTwo = set("asdfghjkl")
        rowThree = set("zxcvbnm")

        result = []

        for word in words:
            word_lower = word.lower()

            if set(word_lower).issubset(rowOne) or \
               set(word_lower).issubset(rowTwo) or \
               set(word_lower).issubset(rowThree):
                result.append(word)

        return result
        