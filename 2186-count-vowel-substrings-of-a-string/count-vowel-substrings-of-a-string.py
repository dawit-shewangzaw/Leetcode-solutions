class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def atMost(k):
            vowels = set('aeiou')
            counts = {}
            left = 0
            ans = 0
            for right in range(len(word)):
                
                if word[right] not in vowels:
                    counts = {}
                    left = right + 1
                    continue
                
                counts[word[right]] = counts.get(word[right], 0) + 1
                
                while len(counts) > k:
                    counts[word[left]] -= 1
                    if counts[word[left]] == 0:
                        del counts[word[left]]
                    left += 1
                
                ans += (right - left + 1)
            return ans

        return atMost(5) - atMost(4)

# class Solution:
#     def countVowelSubstrings(self, word: str) -> int:

#         vowel = "aeiou"
#         count = 0
#         output = 0
#         left = 0

#         for i in range(5):
#             if word[i] in vowel:
#                 count += 1
#                 print("i " + str(word[i]))
#                 print("count for" + str(count))
#             if count == 5:
#                 output += 1
#                 print("output first " + str(output))
                

#         for right in range(5 , len(word)):
#             print("right " + str(word[right]))
            
#             if (word[right]) in vowel:
#                 count += 1
#                 print("count if right" + str(count))
            
#             if (word[left]) in vowel:
#                 count -= 1
#                 print("count if left " + str(count))

#             if count == 5:
#                 output += 1
#                 print("output last " + str(output))
#             left += 1
        
#         return output
        
        # vowel = "aeiou"
        # output = 0
        # max_no = float("-inf")
        # left , right = 0 , k
        # three = ''

        # for _ in range(k):
        #     print(s[_])
        #     three += s[_]
        #     if s[_] in vowel:
        #         output += 1
        #         print(output)
        # max_no = max(max_no , output)
        
        # while right < len(s):
            
        #     if (s[right]) in vowel:
        #         output += 1
            
        #     if (s[left]) in vowel:
        #         output -= 1

        #     right += 1
        #     left += 1
        #     max_no = max(max_no , output)
        # max_no = max(max_no , output)
        
        # return max_no