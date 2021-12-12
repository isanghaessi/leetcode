# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def SLLToList(head):
            result = []
            while head:
                result.append(head.val)
                head = head.next
            return result
        
        converted_list = SLLToList(head)
        return converted_list == converted_list[::-1]
            