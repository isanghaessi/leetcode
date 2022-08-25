from collections import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = deque()
        while head != None:
            nums.append(head.val)
            head = head.next
        while len(nums) > 1:
            if nums.pop() != nums.popleft():
                
                return False
        
        return True
        