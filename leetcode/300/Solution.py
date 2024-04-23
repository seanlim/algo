class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = [nums[0]]
        for n in nums[1:]:
            i, j = 0, len(seq)
            while i < j:
                mid = i + (j - i) // 2
                if seq[mid] == n:
                    i = mid
                    break
                if seq[mid] > n:
                    j = mid
                else:
                    i = mid + 1
            if i > len(seq) - 1:
                seq.append(n)
                continue
            seq[i] = n
        return len(seq)
