# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListNode(head):
            p, q, r = None, head, head
            while q:
                q.next, r = p, q.next
                p, q = q, r
            
            return p
        
        
        def listNodeToList(head):
            resultList = []
            while head:
                resultList.append(head.val)
                head = head.next
            
            return resultList
        
        
        def listToListNode(l):
            resultListNode = node = ListNode()
            for _l in l:
                node.next = ListNode(_l)
                node = node.next
            
            return resultListNode.next
        
        
        l1List, l2List = listNodeToList(reverseListNode(l1)), listNodeToList(reverseListNode(l2))
        
        return reverseListNode(listToListNode([digit for digit in str(int(''.join([str(l1l) for l1l in l1List])) + int(''.join([str(l2l) for l2l in l2List])))]))