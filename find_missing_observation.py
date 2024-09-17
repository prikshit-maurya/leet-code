"""
https://leetcode.com/problems/find-missing-observations/
"""
from typing import List

# Method 1
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        mrs = sum(rolls)
        r = mean*(len(rolls) + n)-mrs

        if r < n or r>(n*6):
            return []
        else:
            mr = [1]*n
            r -= n
            i = 0
            while r > 5:
                mr[i] = mr[i] + 5
                r -= 5
                i += 1
            mr[i] += r
            return mr


obj = Solution()
# print(obj.missingRolls([1,2,3,4], 6, 4))
# print(obj.missingRolls([3,2,4,3], 4, 2))
print(obj.missingRolls([4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5], 4, 40))