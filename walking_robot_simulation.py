"""
https://leetcode.com/problems/walking-robot-simulation/description/
"""
from typing import List

class Solution:
    def fixd(self, d: int)-> int:
        if d < 1:
            return 4
        elif d > 4:
            return 1
        else:
            return d
        
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = y = 0
        d = 1 # 1-> North, 2 -> East, 3-> South, 4 -> West.
        wc = []
        for c in commands:
            if c == -1:
                d += 1
                d = self.fixd(d)
            elif c == -2:
                d -= 1
                d = self.fixd(d)
            else:
                if d == 1:
                    for _ in range(c):
                        if [x, y+1] in obstacles:
                            break
                        else:
                            y += 1
                elif d == 2:
                    for _ in range(c):
                        if [x+1, y] in obstacles:
                            break
                        else:
                            x += 1
                elif d == 3:
                    for _ in range(c):
                        if [x, y-1] in obstacles:
                            break
                        else:
                            y -= 1
                else:
                    for _ in range(c):
                        if [x-1, y] in obstacles:
                            break
                        else:
                            x -= 1
                wc.append((x*x+y*y))
        return max(wc)
    




obj = Solution()
print(obj.robotSim([4,-1,3], []))
print(obj.robotSim([6,-1,-1,6], []))
print(obj.robotSim([4,-1,4,-2,4], [[2,4]]))
print(obj.robotSim([-2,8,3,7,-1], [[-4,-1],[1,-1],[1,4],[5,0],[4,5],[-2,-1],[2,-5],[5,1],[-3,-1],[5,-3]]))
        