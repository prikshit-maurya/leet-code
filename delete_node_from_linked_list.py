"""
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        while True:
            if head.val in nums:
                head = head.next
            else:
                break

        curr_head = head
        next_head = curr_head.next
        while next_head != None:
            if next_head.val in nums:
                next_head = next_head.next
                curr_head.next = next_head
            else:
                curr_head = next_head
                next_head = next_head.next
        
        return head