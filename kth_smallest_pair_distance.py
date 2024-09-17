"""
https://leetcode.com/problems/find-k-th-smallest-pair-distance
"""
from typing import List


# Method 1
# class Solution:
#     def smallestDistancePair(self, numbers: List[int], k: int) -> int:
#         numbers.sort()
#         minDistance, maxDistance = 0, numbers[-1] - numbers[0]
        
#         while minDistance < maxDistance:
#             midDistance = (minDistance + maxDistance) // 2
#             if self.countPairsWithinDistance(numbers, midDistance) < k:
#                 minDistance = midDistance + 1
#             else:
#                 maxDistance = midDistance
        
#         return minDistance

#     def countPairsWithinDistance(self, numbers: List[int], targetDistance: int) -> int:
#         count = left = 0
#         for right in range(1, len(numbers)):
#             while numbers[right] - numbers[left] > targetDistance:
#                 left += 1
#             count += right - left
#         return count



# Method 2
class Solution:

    def getDistance(self, nums: List[int]) -> bool:
        arr: dict = {}
        while len(nums) > 1:
            for i in range(1, len(nums)):
                d = abs(nums[0]-nums[i])
                arr[d] = arr.get(d, 0) + 1
            nums.pop(0)
        return arr
    
    
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        arr = self.getDistance(nums)
        tc = 0
        for s in sorted(arr.keys()):
            tc += arr[s]
            if tc>=k:
                return s
        return None
    

obj = Solution()
print(obj.smallestDistancePair([1,6,1], 3))
    
        