class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowel = "aeiou"
        output = 0
        max_no = float("-inf")
        left , right = 0 , k
        three = ''

        for _ in range(k):
            print(s[_])
            three += s[_]
            if s[_] in vowel:
                output += 1
                print(output)
        max_no = max(max_no , output)
        
        while right < len(s):
            
            if (s[right]) in vowel:
                output += 1
            
            if (s[left]) in vowel:
                output -= 1

            right += 1
            left += 1
            max_no = max(max_no , output)
        max_no = max(max_no , output)
        
        return max_no