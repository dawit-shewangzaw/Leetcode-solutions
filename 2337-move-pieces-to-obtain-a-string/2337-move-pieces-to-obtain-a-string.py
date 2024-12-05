class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove '_' and compare the remaining sequence of 'L' and 'R'
        if start.replace("_", "") != target.replace("_", ""):
            return False

        # Two pointers to verify movement rules
        i, j = 0, 0
        while i < len(start) and j < len(target):
            # Skip '_' in both strings
            while i < len(start) and start[i] == '_':
                i += 1
            while j < len(target) and target[j] == '_':
                j += 1

            # If both pointers are within bounds
            if i < len(start) and j < len(target):
                # Mismatch in positions of 'L' or 'R'
                if start[i] != target[j]:
                    return False
                # Movement rules
                if start[i] == 'L' and i < j:  # 'L' cannot move right
                    return False
                if start[i] == 'R' and i > j:  # 'R' cannot move left
                    return False

                # Move both pointers
                i += 1
                j += 1

        # Ensure no extra pieces are left unmatched
        while i < len(start) and start[i] == '_':
            i += 1
        while j < len(target) and target[j] == '_':
            j += 1

        return i == len(start) and j == len(target)
