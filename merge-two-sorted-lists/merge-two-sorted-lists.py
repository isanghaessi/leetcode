# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def SLLToList(head):
            result = []
            while head:
                result.append(head.val)
                head = head.next
            return result
        
        
        def ListToSLL(list):
            head = temp = ListNode()
            for l in list:
                temp.next = ListNode(l)
                temp = temp.next
            return head.next
        
        
        list1 = SLLToList(list1)
        list2 = SLLToList(list2)
        return ListToSLL(sorted([*list1, *list2]))