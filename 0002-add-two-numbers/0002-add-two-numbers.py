# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize dummy node and current pointer
        dummy = ListNode()
        current = dummy
        carry = 0
        
        # Traverse both lists
        while l1 or l2 or carry:
            # Get values from l1 and l2, or 0 if they've ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            
            # Move to the next nodes
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        # Return the result list
        return dummy.next
