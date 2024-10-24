# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # If both nodes are None, they are trivially flip equivalent
        if not root1 and not root2:
            return True
        # If only one of the nodes is None or the values don't match, return False
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        # Recursively check both possible cases for flip equivalency
        # 1. No flip case: left child with left child, right child with right child
        # 2. Flip case: left child with right child, right child with left child
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
               (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
