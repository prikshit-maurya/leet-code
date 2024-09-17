"""
https://leetcode.com/problems/lemonade-change/
"""
from typing import List

# Method 1
# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         fc = 0
#         tc = 0
#         tw = 0
#         for b in bills:
#             if b == 20:
#                 if tc >= 1 and fc >= 1:
#                     tc -= 1
#                     fc -= 1
#                 elif fc >= 3:
#                     fc -= 3
#                 else:
#                     return False
#                 tw += 1
#             elif b == 10:
#                 if fc >= 1:
#                     fc -= 1
#                 else:
#                     return False
#                 tc += 1
#             else:
#                 fc += 1
#         return True


# Method 2
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fc = 0
        tc = 0
        for b in bills:
            if b == 5:
                fc += 1
            elif b == 10:
                if fc > 0:
                    fc -= 1
                    tc += 1
                else:
                    return False
            else:
                if tc > 0 and fc > 0:
                    fc -= 1
                    tc -= 1
                elif tc < 1 and fc > 2:
                    fc -= 3
                else:
                    return False
        return True


obj = Solution()
print(obj.lemonadeChange([5,5,5,10,20]))
# print(obj.lemonadeChange([5,5,10,10,20]))