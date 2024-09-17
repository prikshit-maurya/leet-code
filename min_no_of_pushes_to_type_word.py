"""
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii
"""
def minimumPushes(word: str) -> int:
    char_count = {}
    word_set = set(word)
    for c in word_set:
        char_count[c] = word.count(c)
    
    char_count_len = len(char_count)
    no_of_button = 8
    iter_range = ((char_count_len//no_of_button)+1) if len(char_count) > no_of_button else 1

    button_pushed_values = [*char_count.values()]
    button_pushed_values.sort(reverse=True)
    count = 0

    for i in range(iter_range):
        s=i*no_of_button
        e=s+no_of_button
        count = count + ((i+1)*sum(button_pushed_values[s:e]))

    return count


word = "xyzxyzxyzxyz"
word = "aabbccddeeffgghhiiiiii"
word = "abzaqsqcyrbzsrvamylmyxdjl"
print(minimumPushes(word))