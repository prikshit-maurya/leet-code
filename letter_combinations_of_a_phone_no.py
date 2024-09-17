"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number
"""
from typing import List

# Method 1
# def letterCombinations(digits: str) -> List[str]:
#     num_to_letter_map = {
#         "2": "abc",
#         "3": "def",
#         "4": "ghi",
#         "5": "jkl",
#         "6": "mno",
#         "7": "pqrs",
#         "8": "tuv",
#         "9": "wxyz"
#     }

#     def combine(str1: List[str], str2: List[str]) -> List[str]:
#         if len(str1) < 1:
#             return str2
#         elif len(str2) < 1:
#             return str1
#         else:
#             ns = []
#             for s1 in str1:
#                 for s2 in str2:
#                     ns.append(s1+s2)
#             return ns

#     combo = []
#     for d in digits:
#         combo = combine(combo, [x for x in num_to_letter_map[d]])
    
#     return combo


# Method 2
# def letterCombinations(digits: str) -> List[str]:
#     num_to_letter_map = {
#         "2": "abc",
#         "3": "def",
#         "4": "ghi",
#         "5": "jkl",
#         "6": "mno",
#         "7": "pqrs",
#         "8": "tuv",
#         "9": "wxyz"
#     }

#     def combine(str1: List[str], str2: List[str]) -> List[str]:
#         if len(str1) < 1:
#             return str2
#         elif len(str2) < 1:
#             return str1
#         else:
#             ns = set()
#             for s1 in str1:
#                 for s2 in str2:
#                     ns.add(s1+s2)
#             return ns

#     combo = set()
#     for d in digits:
#         combo = combine(combo, set(x for x in num_to_letter_map[d]))
    
#     return list(combo)


# Method 3
def letterCombinations(digits: str) -> List[str]:
    num_to_letter_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def combine(str1: List[str], str2: List[str]) -> List[str]:
        if len(str1) < 1:
            return str2
        elif len(str2) < 1:
            return str1
        else:
            ns = set()
            for s1 in str1:
                _str2 = ','+",".join(str2)
                _str2 = _str2.replace(",",','+s1)
                _str2 = _str2.strip(",")
                ns = ns.union(set(_str2.split(",")))

            return ns

    combo = set()
    for d in digits:
        combo = combine(combo, set(x for x in num_to_letter_map[d]))
    
    return list(combo)


print(letterCombinations("23"))