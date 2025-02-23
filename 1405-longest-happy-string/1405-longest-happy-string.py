class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))
        
        result = []
        
        while max_heap:
            count1, char1 = heapq.heappop(max_heap)
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not max_heap:
                    break
                count2, char2 = heapq.heappop(max_heap)
                result.append(char2)
                if count2 + 1 < 0:
                    heapq.heappush(max_heap, (count2 + 1, char2))
                heapq.heappush(max_heap, (count1, char1))
            else:
                result.append(char1)
                if count1 + 1 < 0:
                    heapq.heappush(max_heap, (count1 + 1, char1))
        
        return ''.join(result)
