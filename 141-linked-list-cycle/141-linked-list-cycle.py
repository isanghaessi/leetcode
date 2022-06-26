# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        oneStep = twoStep = head
        while oneStep != None and twoStep != None:
            oneStep = oneStep.next
            if twoStep.next == None:
                
                return False
            twoStep = twoStep.next.next
            if oneStep == twoStep:
                
                return True
            
            
        return False