"""
https://leetcode.com/problems/integer-to-english-words/
"""

# Method 1
    # def numberToWords(num: int) -> str:

    #     def numberToWordsHelper(num: int) -> str:
    #         digitString = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    #         teenString = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    #         tenString = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            
    #         result = ""
    #         if num > 99:
    #             result += digitString[num // 100] + " Hundred "
            
    #         num %= 100
    #         if num < 20 and num > 9:
    #             result += teenString[num - 10] + " "
    #         else:
    #             if num >= 20:
    #                 result += tenString[num // 10] + " "
    #             num %= 10
    #             if num > 0:
    #                 result += digitString[num] + " "
            
    #         return result

    #     if num == 0:
    #         return "Zero"
        
    #     bigString = ["Thousand", "Million", "Billion"]
    #     result = numberToWordsHelper(num % 1000)
    #     num //= 1000
        
    #     for i in range(len(bigString)):
    #         if num > 0 and num % 1000 > 0:
    #             result = numberToWordsHelper(num % 1000) + bigString[i] + " " + result
    #         num //= 1000
        
    #     return result.strip()

        

# Method 2
def numberToWords(num: int) -> str:
    hun_mapping = {
        100:"Hundred",
        1000:"Thousand",
        1000000:"Million",
        1000000000:"Billion"
    }

    ones  = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]  
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens  = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def getWord(_num: int, add_one: bool=False) -> str:
        if _num in hun_mapping:
            if add_one or num in hun_mapping:
                return getWord(1) +' '+ hun_mapping[_num]
            else:
                return hun_mapping[_num]
        elif _num < 10:
            return ones[_num]
        elif _num < 20:
            if _num %10 == 0:
                return tens[(_num%10)+1]
            else:
                return teens[_num%10]
        elif _num < 100:
            if _num %10 == 0:
                return tens[_num//10]
            else:
                return tens[_num//10] +" "+ getWord((_num%10), False)
        else:
            _times = int('1'+'0'*(len(str(_num))-1))
            
            import pdb; pdb.set_trace()
            if (_num%100 == 0) and (_num%_times in hun_mapping):
                add_one = True

            while _times > 100 and _times not in hun_mapping:
                _times = _times/10

            return ("" if (_num/_times) < 1 else getWord(int(_num/_times), False)) + ' ' + getWord(_times, False) + ' ' + (getWord(int(_num%_times), add_one) if int(_num%_times)>0 else "")

    word = getWord(num).strip()
    return word


# num=100
# num=123
# num=200
# num=1000
# num=1100
# num=1230
# num=2100
# num=12345
num=100000
# num=1234567
print(numberToWords(num))
   