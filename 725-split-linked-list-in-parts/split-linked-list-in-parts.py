# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        N = 0
        while curr:
            N += 1
            curr = curr.next
            
        base_size = N // k
        remainder = N % k
        
        result = []
        curr = head
        
        for i in range(k):
            part_size = base_size + (1 if i < remainder else 0)
            
            if not curr:
                result.append(None)
                continue
            
            result.append(curr)
            
            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next
            
            if curr:
                next_part_head = curr.next
                curr.next = None
                curr = next_part_head
                
        return result 