# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        level_sums = []
        queue = deque([root])
        
        # Perform level-order traversal (BFS)
        while queue:
            level_sum = 0
            level_size = len(queue)
            
            # Process each node in the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # Add child nodes to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add the current level's sum to the list
            level_sums.append(level_sum)
        
        # Sort level sums in descending order
        level_sums.sort(reverse=True)
        
        # Return the k-th largest level sum or -1 if there are fewer than k levels
        if k > len(level_sums):
            return -1
        else:
            return level_sums[k - 1]
