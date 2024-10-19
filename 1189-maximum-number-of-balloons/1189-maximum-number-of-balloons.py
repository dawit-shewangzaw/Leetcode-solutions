from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count the occurrences of each character in the text
        char_count = Counter(text)
        
        # Count how many times "balloon" can be formed
        # We need 1 'b', 1 'a', 2 'l's, 2 'o's, 1 'n'
        b_count = char_count['b']
        a_count = char_count['a']
        l_count = char_count['l'] // 2  # 'l' is needed twice
        o_count = char_count['o'] // 2  # 'o' is needed twice
        n_count = char_count['n']
        
        # The limiting factor is the minimum number of instances we can form
        return min(b_count, a_count, l_count, o_count, n_count)
