class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def backtrack(start: int, path: List[str]):
            if start == len(s):
                result.append(path[:])  # Add a copy of the current path to the result
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)  # Choose
                    backtrack(end, path)   # Explore
                    path.pop()            # Un-choose
        
        result = []
        backtrack(0, [])
        return result
