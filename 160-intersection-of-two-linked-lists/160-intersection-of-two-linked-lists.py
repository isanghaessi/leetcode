# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    firstNode = ListNode(None)
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def lltol(ll):
            l = []
            while ll != None:
                l.append(ll)
                ll = ll.next
            l.append(self.firstNode)
            
            return l
        
        
        reversedListA, reversedListB = lltol(headA)[::-1], lltol(headB)[::-1]
        i = 0
        while i < len(reversedListA) and i < len(reversedListB):
            if id(reversedListA[i]) != id(reversedListB[i]):
                if i == 0:
                    
                    return None
                
                return reversedListA[i].next
            i = i + 1

        return reversedListA[i - 1]