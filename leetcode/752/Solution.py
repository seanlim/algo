from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque([("0000", 0)])
        visited = set(deadends)
        while q:
            n, nSteps = q.popleft()
            if n == target:
                return nSteps
            if n in visited:
                continue
            visited.add(n)
            for i in range(4):
                digit = int(n[i])
                digit0 = (digit + 1) % 10
                digit1 = (digit - 1) % 10
                for d in [digit0, digit1]:
                    q.append((n[:i] + str(d) + n[i + 1 :], nSteps + 1))
        return -1
