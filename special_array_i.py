"""
https://leetcode.com/problems/special-array-i/
"""

from typing import List

# Method 1
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if (nums[i-1] + nums[i])%2==0:
                return False
        return True