"""
https://leetcode.com/problems/combination-sum-ii/
"""
from typing import List

# Method 1
# class Solution:
#     def combinationSum2(self, cand, target):
#         cand.sort()
#         res = []
#         path = []
#         self.dfs(cand, 0, target, path, res)
#         return res
    
#     def dfs(self, cand, cur, target, path, res):
#         if target == 0:
#             res.append(path.copy())
#             return
#         if target < 0:
#             return
        
#         for i in range(cur, len(cand)):
#             if i > cur and cand[i] == cand[i - 1]:  # Skip duplicates
#                 continue
#             path.append(cand[i])
#             self.dfs(cand, i + 1, target - cand[i], path, res)
#             path.pop()  # Backtrack



# Method 2
class Solution:

    def getConbinations(self, arr: List[int], target: int) -> List[List[int]]:
        new_arr: List[List[int]] = []
        arr_len: int = len(arr)
        
        if arr_len < 1 and sum(arr) == target:
            return arr
        elif arr_len == 1 and sum(arr) == target:
            return arr
        else:
            for i in range(0, arr_len-1):
                if i!= 0 and (arr[i] == arr[i-1]):
                    continue

                for j in range(i+1, arr_len):
                    temp_arr = arr[i:i+1]+arr[i+1:i+j]
                    temp_sum = sum(temp_arr)
                    if temp_sum < target:
                        continue
                    elif temp_sum == target:
                        new_arr.append(temp_arr)
                    else: break

            return new_arr


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combi = self.getConbinations(candidates, target)
        return combi




obj = Solution()
print(obj.combinationSum2([1,1,2,3], 4))
# print(obj.combinationSum2([1,1,2,5,6,7,10], 8))