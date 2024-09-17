"""
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
"""
from typing import List

# Method 1
# def rangeSum(nums: List[int], n: int, left: int, right: int) -> int:
#     nar = []
#     for i in range(n):
#         for j in range(i+1,n+1):
#             nar.append(sum(nums[i:j]))

#     nar.sort()
#     return sum(nar[left-1:right])%1000000007
    

# Method 2
def rangeSum(nums: List[int], n: int, left: int, right: int) -> int:
    nar = []
    for i in range(n):
        t=nums[i]
        nar.append(t)
        for _n in nums[i+1:]:
            t = t+_n
            nar.append(t)

    nar.sort()
    return sum(nar[left-1:right])%1000000007
    


# n,l,r=[1,2,3,4], 1, 5
# n,l,r=[1,2,3,4], 3, 4
n,l,r=[1,2,3,4], 1, 10
print(rangeSum(n,len(n),l,r))


