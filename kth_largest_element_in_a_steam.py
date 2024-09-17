"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()
        self.nums= self.nums[-self.k:]
        self.number = None
        
    def insert(self, num: int, nums: List[int]):
        nl = len(nums)
        if nl < 1:
            return [num]

        i = nl >> 1
        if nums[i] < num:
            return nums[:i+1] + self.insert(num, nums[i+1:])
        else:
            return self.insert(num, nums[:i]) + nums[i:]
        
    def add(self, val: int) -> int:
        if self.number == None or val >= self.number:
            self.nums = self.insert(val, self.nums)
            if len(self.nums) > self.k:
                self.nums = self.nums[1:]
            self.number = self.nums[0]
        return self.number


# obj: KthLargest = KthLargest(3, [4, 5, 8, 2])
# print(obj.add(3))
# print(obj.add(5))
# print(obj.add(10))
# print(obj.add(9))
# print(obj.add(4))

# obj: KthLargest = KthLargest(1, [])
# print(obj.add(-3))
# print(obj.add(-2))
# print(obj.add(-4))
# print(obj.add(0))
# print(obj.add(4))

obj: KthLargest = KthLargest(2, [0])
print(obj.add(-1))
print(obj.add(1))
print(obj.add(-2))
print(obj.add(-4))
print(obj.add(3))



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)