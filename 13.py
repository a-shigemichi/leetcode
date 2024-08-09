class Solution:
    def romanToInt(self, s: str) -> int:
        Integer_word = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum = 0
        num = 1
        for char in reversed(s):
            if Integer_word[char] < num:
                word_sign = -1
            else:
                word_sign = 1
            num = Integer_word[char]
            sum += word_sign*Integer_word[char]
        return sum