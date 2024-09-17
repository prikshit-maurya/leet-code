"""
https://leetcode.com/problems/two-sum/
"""

# Method 1
# def two_sum(nums, target):
#     d={}
#     index = []
#     for i,n in enumerate(nums):
#         s=target-n
#         if n in d:
#             index = [d[n], i]
#         else:
#             d[s] = i
#     return index


# Method 2
def two_sum(nums, target):
    d={}
    index = []
    l = len(nums)-1
    isEven = len(nums)%2
    nby2 = len(nums)//2 + (0 if isEven else 1)
    for i in range(0, nby2+1):
        s=target-nums[i]
        if nums[i] in d:
            index = [d[nums[i]], i]
            break
        else:
            d[s] = i
        
        if i<(l//2 + (0 if isEven else 1)) :
            s=target-nums[l-i]
            if nums[l-i] in d:
                index = [d[nums[l-i]], l-i]
                break
            else:
                d[s] = l-i
    return index


print(two_sum([1,2,3,0,4,5], 9))
# print(two_sum([0,4,3,0], 0))