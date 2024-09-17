"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
# Method 1
# def find_sub_str(s: str):
#     hl = 0
#     for i in range(len(s)):
#         cs, l = "", 0
#         for c in s[i:]:
#             if c in cs:
#                 break
#             else:
#                 cs += c
#                 l += 1
#         hl = l if l>hl else hl
#     return hl


# Method 2:
# def find_sub_str(s: str):
#     hl = 0
#     lp = 0
#     l = 0

#     # import pdb; pdb.set_trace()
#     for rp in range(0, len(s)):
#         c = s[rp]
#         if (lp!=rp) & (c in s[lp:rp]):
#             hl = l if l>hl else hl
#             lp = len(s[:lp]) + s[lp:rp].index(c) + 1
#             l  = len(s[lp:rp]) + 1
#         else:
#             l += 1

#     hl = l if l>hl else hl
#     return hl


# Method 3:
def find_sub_str(s: str):
    _ss = ""
    hl = 0
    l = 0
    for _s in s:
        if _s in _ss:
            _ss = _ss.split(_s)[1]
            _ss += _s
            hl = hl if hl>l else l
            l = len(_ss)
        else:
            _ss += _s
            l += 1
    
    hl = hl if hl>l else l
    return hl    

# _s = "bbbbb"
# _s = "abcabcbb"
# _s = "pwwkew"
# _s = "au"
_s = ""
print(find_sub_str(_s))
                
