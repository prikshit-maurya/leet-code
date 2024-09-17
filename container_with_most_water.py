"""
https://leetcode.com/problems/container-with-most-water/
"""
from typing import List

# class Solution:
#     def getVolume(self, l: List[int]) -> int:
#         l_len = len(l)
#         if l_len < 1:
#             return 0

#         v = set()
#         for i in range(1, l_len):
#             v.add(min(l[0], l[i])*i)

#         return max(v) if len(v)>0 else 0
        
#     def maxArea(self, height: List[int]) -> int:
#         m = 0
#         ln = 0
#         for i in range(len(height)):
#             if height[i] < ln:
#                 continue
#             m = max(m, self.getVolume(height[i:]))
#             ln = height[i]
#         return m
    

class Solution:

    def maxArea(self, height: List[int]) -> int:
        li = 0
        ri = len(height)-1
        a = 0
        while li < ri:
            if height[li] < height[ri]:
                a = max(a, height[li]*(ri-li))
                li += 1
            else:
                a = max(a, height[ri]*(ri-li))
                ri -= 1
        return a


obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
