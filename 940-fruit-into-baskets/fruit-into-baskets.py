class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0
        max_fruits = 0
        
        for right in range(len(fruits)):
            fruit_type = fruits[right]
            count[fruit_type] = count.get(fruit_type, 0) + 1
            
            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                
                if count[left_fruit] == 0:
                    del count[left_fruit]
                
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits