"""
https://leetcode.com/problems/2-keys-keyboard/
"""
from typing import List

class Solution:
    pn: List[int] = [2]
    def __init__(self):
        for i in range(2,1000):
            if self.isPrime(i):
                self.pn.append(i)

    def isPrime(self, n:int) -> bool:
        if n%2 == 0:
            return False
        for i in range(3, n//2, 2):
            if n%i == 0:
                return False
        return True
        
    def minSteps(self, n: int) -> int:
        if n in self.pn:
            return n
        else:
            f = []
            break_main = False
            while n > 3:
                for _n in self.pn:
                    if n%_n == 0:
                        n = n // _n
                        f.append(_n)
                        if n in self.pn:
                            f.append(n)
                            break_main = True
                        break
                if break_main:
                    break
            return sum(f)
            
obj = Solution()
print(obj.minSteps(757))