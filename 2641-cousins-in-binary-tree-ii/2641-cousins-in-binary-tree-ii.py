from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # Use a queue for level-order traversal
        queue = deque([root])
        root.val = 0  # The root node has no cousins, so set its value to 0.
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            nodes_at_level = []
            
            # First pass: collect nodes at the current level and calculate the level_sum
            for _ in range(level_size):
                node = queue.popleft()
                nodes_at_level.append(node)
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                    level_sum += node.left.val
                if node.right:
                    queue.append(node.right)
                    level_sum += node.right.val
            
            # Second pass: update each node's children based on cousin sums
            for node in nodes_at_level:
                if node.left and node.right:
                    sibling_sum = node.left.val + node.right.val
                    node.left.val = level_sum - sibling_sum  # Exclude siblings
                    node.right.val = level_sum - sibling_sum  # Exclude siblings
                elif node.left:
                    node.left.val = level_sum - node.left.val  # Exclude itself (no sibling)
                elif node.right:
                    node.right.val = level_sum - node.right.val  # Exclude itself (no sibling)
        
        return root
