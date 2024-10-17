from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Count the frequency of each element in the array
        frequency = Counter(arr)
        
        # Extract the frequencies and check if they are unique
        occurrences = list(frequency.values())
        
        # Use a set to check for uniqueness (sets do not allow duplicates)
        return len(occurrences) == len(set(occurrences))
