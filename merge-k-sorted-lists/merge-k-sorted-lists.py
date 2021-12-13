import functools

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def SLLToList(head):
            result = []
            while head:
                result.append(head.val)
                head = head.next
            return result
        
        
        def ListToSLL(_list):
            head = temp = ListNode()
            for _l in _list:
                temp.next = ListNode(_l)
                temp = temp.next
            return head.next
        
        
        return ListToSLL(sorted(functools.reduce(lambda acc, a: [*acc, *a], (map(SLLToList, lists)), [])))