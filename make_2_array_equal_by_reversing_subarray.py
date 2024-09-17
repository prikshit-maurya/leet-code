"""
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays
"""

from typing import List

def make_equal(target: List[int], arr: List[int]) ->  bool:
    target.sort()
    arr.sort()

    return tuple(target) == tuple(arr)