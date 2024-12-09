# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the tree is empty
        if not root:
            return 0
        
        # Recursively calculate the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The depth of the current node is the max of left and right depths + 1
        return max(left_depth, right_depth) + 1
