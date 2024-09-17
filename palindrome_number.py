"""
https://leetcode.com/problems/palindrome-number/
"""

# Method 1
# def isPalindrome(num:int) -> bool:
#     num = str(num)
#     lp = 0
#     rp = len(num)
#     status = True
#     while lp < rp:
#         if num[lp] != num[rp-1]:
#             status=False
#             break
#         lp +=1
#         rp -=1
#     return status


# Method 2
# def isPalindrome(x:int) -> bool:
#     num = str(x)
#     return num == num[::-1]


# Method 3
# def isPalindrome(x:int) -> bool:
#     num = str(x)
#     l = len(num)
#     for i in range(l):
#         if num[i] != num[l-i-1]:
#             return False
#     return True


# Method 4
def isPalindrome(x:int) -> bool:
    if x < 0:
        return False
    elif x<10:
        return True
    else:
        num = str(x)
        return num == num[::-1]
        

n=121
# n=-121
# n=10
# n=1
print(isPalindrome(n))



