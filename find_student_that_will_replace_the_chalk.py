"""
https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
"""
from typing import List

# Method 1
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalk_sum = sum(chalk)
        k = k%chalk_sum
        if k == 0:
            return 0
        for i in range(len(chalk)):
            if chalk[i] <= k:
                k -= chalk[i]
            else:
                break
        return i
    

obj = Solution()
print(obj.chalkReplacer([5,1,5], 23))
print(obj.chalkReplacer([3,4,1,2], 25))
print(obj.chalkReplacer([1], 1000000000))