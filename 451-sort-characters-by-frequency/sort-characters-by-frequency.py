class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: count frequency
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Step 2: convert to list and sort
        items = list(freq.items())
        items.sort(key=lambda x: x[1], reverse=True)
        print(items)
        
        # Step 3: build result
        result = ""
        for char, count in items:
            for i in range(count):
                result += char
            print(count , char)
        
        return result