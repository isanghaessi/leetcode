# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            
            return None
        elif list1 != None and list2 == None:
            node = list1
            node.next = self.mergeTwoLists(node.next, list2)
            
            return node
        elif list1 == None and list2 != None:
            node = list2
            node.next = self.mergeTwoLists(list1, node.next)
            
            return node
        else:
            if list1.val <= list2.val:
                node = list1
                node.next = self.mergeTwoLists(node.next, list2)
            else:
                node = list2
                node.next = self.mergeTwoLists(list1, node.next)
            
            return node
        
        