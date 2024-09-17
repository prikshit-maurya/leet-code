"""
https://leetcode.com/problems/spiral-matrix-iv/
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [-1]*n
        mat = [mat]*m
        d = 0 # 0->right, 1->down, 2->left, 3->up

        i = si = 0
        j = sj = 0
        ei, ej = n, m
        c = 0

        while c < (m*n):
            if d == 0:




        for m in mat:
            print(m)


        



        
                    






obj = Solution()
print(obj.spiralMatrix(5,5,[3,0,2,6,8,1,7,9,4,2,5,5,0]))