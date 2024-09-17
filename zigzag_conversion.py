"""
https://leetcode.com/problems/zigzag-conversion/
"""

# Method 1 : Didn't work
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         ns = ""
#         sl = len(s)
#         gp = numRows + numRows - 2
#         if gp < 1:
#             return s

#         cl = sl%gp+1
#         for r in range(numRows):
#             i = r
#             if i in (0, numRows-1):
#                 while i < sl:
#                     ns += s[i] if i < sl else ''
#                     i  += gp
#             else:
#                 if r < numRows:
#                     ns += s[r] if r < sl else ''

#                 for j in range(1, (cl+1)):
#                     idx = gp*j
#                     ns += s[idx-r] if (idx-r) < sl else ""
#                     ns += s[idx+r] if (idx+r) < sl else ""

#         return ns


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ns = {}
        d = "u" # u -> increase, d -> decrease
            
        c = 0
        i = 0
        while c<len(s):
            print(i)
            ns[i] = ns.get(i, "")+s[c]
            i += 1 if d == 'u' else -1
            if i<0:
                d="u"
                i=1
            elif i == numRows:
                d="d"
                i=numRows-2
            c += 1
        
        # print(ns)
        return ""

obj = Solution()
print(obj.convert("PAYPALISHIRING", 3)) # PAHNAPLSIIGYIR
# print(obj.convert("PAYPALISHIRING", 4)) # PINALSIGYAHRPI
# print(obj.convert("A", 1)) # A
