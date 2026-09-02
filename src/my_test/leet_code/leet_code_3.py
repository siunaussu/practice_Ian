def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    max_len = 0
    for right, c in enumerate(s):
        if c in char_index:
            left = max(left, char_index[c] + 1)
            print("left:", left)
        char_index[c] = right
        print("char_index:", char_index)
        max_len = max(max_len, right - left + 1)
    return max_len

a = "abcc"
print(lengthOfLongestSubstring(a))
