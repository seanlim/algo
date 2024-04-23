class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        cnt = 0
        for i in range(len(height)):
            maxLeft[i] = cnt
            cnt = max(height[i], cnt)
        cnt = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = cnt
            cnt = max(height[i], cnt)
        print(maxLeft, maxRight)
        area = 0
        for i in range(len(height)):
            # print(f"water height: {min(maxRight[i], maxLeft[i])}")
            waterDepth = min(maxRight[i], maxLeft[i])
            if waterDepth > height[i]:
                area += waterDepth - height[i]
        return area
