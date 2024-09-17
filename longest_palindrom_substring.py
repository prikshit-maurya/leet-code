"""
https://leetcode.com/problems/longest-palindromic-substring/description/
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_ps = ""
        max_pl = 0
        for i in range(len(s)-1):
            if max_pl > len(s[i:]):
                break
            for j in range(i+1, len(s)):
                if s[i:i+1] == s[j:j+1]:
                    ts = s[i:j+1]
                    if ts == ts[::-1]:
                        if len(ts) > max_pl:
                            max_pl = len(ts)
                            max_ps = ts
        if max_pl == 0:
            max_ps = s[0]
        return max_ps



obj = Solution()
# print(obj.longestPalindrome("babad"))
print(obj.longestPalindrome("b"))