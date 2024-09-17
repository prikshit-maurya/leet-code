"""
https://leetcode.com/problems/powx-n/
"""

class Solution:
    def _pow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        t = self._pow(x, n//2)
        if n%2 == 1:
            return t*t*x
        else:
            return t*t
        
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        p = self._pow(x, abs(n))
        return p if n > 0 else 1/p


obj = Solution()
print(obj.myPow(2,10))


