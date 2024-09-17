"""
https://leetcode.com/problems/median-of-two-sorted-arrays
"""
from typing import List

# Method 1
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums = nums1+nums2
    nums.sort()
    l = len(nums)
    l2 = l//2
    med = (nums[l2-1]+nums[l2])/2 if l%2 == 0 else nums[l2]
    return float(med)