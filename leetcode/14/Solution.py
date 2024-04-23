class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        i, j = 0, 1
        maxStrLen = max([len(s) for s in strs])
        prefixes = [s[i:j] for s in strs]
        while all([prefixes[0] == s for s in prefixes]):
            j += 1
            if j > maxStrLen:
                break
            prefixes = [s[i:j] for s in strs]
        return prefixes[0][i : j - 1]
