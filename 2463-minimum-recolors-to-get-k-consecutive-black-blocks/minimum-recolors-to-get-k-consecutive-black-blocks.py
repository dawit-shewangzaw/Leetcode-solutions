class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        output = 0
        black_count = 0
        min_value = float("+inf")
        left = 0

        if k > len(blocks):
            return 0

        for i in range(k):
            
            if blocks[i] == 'B':
                black_count += 1            
            if black_count == k:
                return 0
        
        output = k - black_count
        min_value = min(min_value , output)

        for right in range(k , len(blocks)):
            
            if blocks[right] == 'B':
                black_count += 1
            if blocks[left] == 'B':
                black_count -= 1
            if  black_count == k:
                return 0

            left += 1
            output = k - black_count
            min_value = min(min_value , output)
        
        return min_value

        # black_count = 0
        # ans = float("inf")
        # for i in range(len(blocks)):
        #     if i - k >= 0 and blocks[i - k] == 'B': 
        #         black_count -= 1
        #     if blocks[i] == 'B':
        #         black_count += 1            
        #     ans = min(ans, k - black_count)
        
        # return ans