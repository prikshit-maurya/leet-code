"""
https://leetcode.com/problems/3sum/
"""
from typing import List

# Method 1
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         l = len(nums)
#         ans = set()
#         for i in range(l-2):
#             j = i+1
#             k = l-1
#             while j<k:
#                 s = nums[i]+nums[j]+nums[k]
#                 if s<0:
#                     j+=1
#                 elif s>0:
#                     k-=1
#                 else:
#                     ans.add((nums[i], nums[j], nums[k]))
#                     j+=1
#         return ans


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        ans = set()
        for i in range(l-2):
            if nums[i]>0:
                continue
            for j in range(i+1, l-1):
                if nums[i]+nums[j] > 0:
                    continue
                for k in range(j+1, l):
                    s = nums[i]+nums[j]+nums[k]
                    if s>0:
                        continue
                    elif s==0:
                        ans.add((nums[i]+nums[j]+nums[k]))

        return ans
        
obj = Solution()
obj.threeSum([-1,0,1,2,-1,-4])
