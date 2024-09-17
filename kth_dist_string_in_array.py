"""
https://leetcode.com/problems/kth-distinct-string-in-an-array
"""
from typing import List


# Method 1
# def kthDistinct(arr: List[str], k: int) -> str:
#     na = []
#     ma = set()
#     for i in range(len(arr)):
#         if (arr[i] not in arr[i+1:]) & (arr[i] not in ma):
#             na.append(arr[i])
#         else:
#             ma.add(arr[i])
#     if k <= len(na):
#         return na[k-1]
#     else:
#         return ""
    

# Method 2
# def kthDistinct(arr: List[str], k: int) -> str:
#     na = {}
#     for i in range(len(arr)):
#         na[arr[i]] = na.get(arr[i],0) + 1
#     i = 0
#     v = ""
#     for key in na.keys():
#         if na[key] == 1:
#             i += 1
#             if i == k:
#                 v = key
#                 break

#     return v


# Method 3
def kthDistinct(arr: List[str], k: int) -> str:
    na = {}
    for i in range(len(arr)):
        na[arr[i]] = na.get(arr[i],0) + 1

    narr = []
    for key in na:
        if na[key] < 2:
            narr.append(key)

    if k <= len(narr):
        return narr[k-1]
    else:
        return ""



arr = ["d","b","c","b","c","a"]
# arr = ["aaa","aa","a"]
# arr = ["a","b","a","c"]
print(kthDistinct(arr, 2))
