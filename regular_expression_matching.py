"""
https://leetcode.com/problems/regular-expression-matching/
"""

class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        if ("." not in s) and ("*" not in s):
            return s == p
        else:
            i = 0
            for _s in s:
                
                if p[i] == "*":










obj = Solution()
obj.isMatch("aa", "a")