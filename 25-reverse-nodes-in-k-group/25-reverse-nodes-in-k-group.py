# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        answer = left = ListNode(0, head)
        while left:
            right = left.next
            stack = []
            isK = True
            for _ in range(k):
                if not right:
                    isK = False
                    
                    break
                stack.append(right)
                right = right.next
            if not isK:
                
                break
            else:
                while len(stack) > 0:
                    left.next = stack.pop()
                    left = left.next
                left.next = right
                
        return answer.next
                