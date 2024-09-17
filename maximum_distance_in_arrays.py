"""
https://leetcode.com/problems/maximum-distance-in-arrays/
"""
from typing import List


class Solution(object):
    def maxDistance(self, arrays):
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0

        for arr in arrays[1:]:
            max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])

        return max_distance
    
    
obj = Solution()
# print(obj.maxDistance([[1,2,3],[4,5],[1,2,3]]))
# print(obj.maxDistance([[1,4],[0,5]]))
# print(obj.maxDistance([[1,5],[3,4]]))
# print(obj.maxDistance([[1,4,5],[0,2]]))
# print(obj.maxDistance([[-2],[-3,-2,1]]))
print(obj.maxDistance([[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]))
# print(obj.maxDistance([[-10,-9,-9,-3,-1,-1,0],[-5],[4],[-8],[-9,-6,-5,-4,-2,2,3],[-3,-3,-2,-1,0]]))