# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        before_sub = dummy
        
        for _ in range(left - 1):
            before_sub = before_sub.next
            
        start = before_sub.next
        then = start.next
        
        for _ in range(right - left):
            start.next = then.next
            then.next = before_sub.next
            before_sub.next = then
            then = start.next
            
        return dummy.next