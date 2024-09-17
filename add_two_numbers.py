from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Method 1:
# class Solution:
#     def gen_list_and_reverse(self, tl: Optional[ListNode]):
#         tl = tl.__dict__
#         return str((self.gen_list_and_reverse(tl['next']) if tl['next'] else '')) +','+ str(tl['val'])

#     def gen_listnode_from_str(self, tl: str):
#         if tl > 9:
#             ntl = ListNode(int(tl%10))
#             if int(tl):
#                 ntl.next = self.gen_listnode_from_str(int(str(tl)[:-1]))
#             else:
#                 return None
#         else:
#             ntl = ListNode(tl)
#             ntl.next = None
#         return ntl

#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         l1 = int(self.gen_list_and_reverse(l1).replace(",",""))
#         l2 = int(self.gen_list_and_reverse(l2).replace(",",""))
#         l3 = l1 + l2
#         return self.gen_listnode_from_str(l3)
    

# Method 2:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def add(l1: Optional[ListNode], l2: Optional[ListNode], carry:int=0) -> Optional[ListNode]:

            if not (isinstance(l1, ListNode) or isinstance(l2, ListNode)):
                return ListNode(carry, None) if carry else None

            l1_val = 0 if l1==None else l1.val
            l2_val = 0 if l2==None else l2.val
            l1_next = None if l1==None else l1.next
            l2_next = None if l2==None else l2.next

            tmp_sum = l1_val + l2_val + carry
            carry = int(tmp_sum/10)

            return ListNode(tmp_sum%10, add(l1_next, l2_next, carry))

        return add(l1, l2)
        