"""
https://leetcode.com/problems/bitwise-and-of-numbers-range
"""

def biwise_and_no_range(left: int, right: int) -> int:
    return -1<<(left^right).bit_length()&left


l, r = 1, 2147483647
print(biwise_and_no_range(l, r))