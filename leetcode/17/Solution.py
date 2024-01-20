
mapping = {
    "2": ["a", "b", "c"],
    "8": ["t", "u", "v"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


class Solution(object):
    def letterCombinations(self, digits, arr=[]):
        if digits == "":
            return arr
        chars = mapping[digits[0]]
        if arr == []:
            return self.letterCombinations(digits[1:], chars)
        new_arr = []
        for c in chars:
            new_arr = new_arr + [i + c for i in arr]
        return self.letterCombinations(digits[1:], new_arr)
