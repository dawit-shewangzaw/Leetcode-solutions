class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        vowels = set("aeiou")
        total = 0
        left = 0
        mid = 0
        count = {}

        for right in range(len(word)):
            # 1. If we hit a consonant, reset everything
            if word[right] not in vowels:
                count.clear()
                left = mid = right + 1
                continue

            count[word[right]] = count.get(word[right], 0) + 1

            while len(count) == 5:
                count[word[mid]] -= 1
                if count[word[mid]] == 0:
                    del count[word[mid]]
                mid += 1
            
            total += (mid - left)

        return total   