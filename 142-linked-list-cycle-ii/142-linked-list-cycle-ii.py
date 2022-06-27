# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = []
        i = 0
        while head != None:
            if head in visited:
                
                return head
            visited.append(head)
            head = head.next
            i = i + 1
            
        return None