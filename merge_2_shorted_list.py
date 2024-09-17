"""
https://leetcode.com/problems/merge-two-sorted-lists/description/
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if (list1 == None) & (list2 == None):
        return ListNode('', None)
    elif list1 == None:
        return ListNode(list2.val, list2.next)
    elif list2 == None:
        return ListNode(list1.val, list1.next)
    elif list1.val < list2.val:
        return ListNode(list1.val, mergeTwoLists(list1.next, list2))
    else:
        return ListNode(list2.val, mergeTwoLists(list1, list2.next))