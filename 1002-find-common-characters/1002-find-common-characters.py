from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common_counts = Counter(words[0])
        
        for word in words[1:]:
            word_count = Counter(word)
            common_counts &= word_count  # Intersect counts to find common characters
        
        return list(common_counts.elements())
