# Recursively divide number down and collect roman numerals

div = [1000, 900, 500, 400,  100, 90,  50, 40, 10, 9, 5, 4, 1]
chars = ["M", "CM", "D", "CD",  "C", "XC",
         "L", "XL", "X", "IX",  "V", "IV", "I"]


class Solution(object):
    def intToRoman(self, num):
        res = ""
        curr = 0
        while num < div[curr] and curr < len(div) + 1:
            curr = curr + 1
        remainder = num % div[curr]
        div_result = num // div[curr]
        res = res.join([chars[curr]] * (div_result))
        # Done
        if remainder == 0:
            return res
        return res + self.intToRoman(remainder)
