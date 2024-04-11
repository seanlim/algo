class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        digits[i]+=1
        while digits[i] == 10:
            digits[i] = 0
            if i-1 < 0:
                digits.insert(0, 1)
            else:
                digits[i-1]+=1
            i-=1
        return digits