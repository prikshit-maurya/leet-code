"""
https://leetcode.com/contest/biweekly-contest-137/problems/find-the-power-of-k-size-subarrays-i/
https://leetcode.com/contest/biweekly-contest-137/problems/find-the-power-of-k-size-subarrays-ii/
https://leetcode.com/contest/biweekly-contest-137/problems/maximum-value-sum-by-placing-three-rooks-i/
https://leetcode.com/contest/biweekly-contest-137/problems/maximum-value-sum-by-placing-three-rooks-ii/
"""
from typing import List

class Solution:
    def isConsAndSorted(self, n: List[int])->bool:
        _n = n[-1]-n[0]+1
        _sum = (_n/2)*(n[0]+n[-1])
        return sum(n) == _sum

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        results: List[int] = []
        for i in range(len(nums)-k+1):
            if not self.isConsAndSorted(nums[i:i+k]):
                results.append(-1)
            else:
                results.append(nums[i:i+k][-1])
            
        return results



# obj = Solution()
# print(obj.resultsArray([1,2,3,4,3,2,5], 3))
# print(obj.resultsArray([2,2,2,2,2], 4))
# print(obj.resultsArray([3,2,3,2,3,2], 2))
# print(obj.resultsArray([1,2,3,4,3,2,5], 3))