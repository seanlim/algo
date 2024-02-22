class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = None
        maxProfit = 0
        for price in prices:
            if minPrice != None:
                maxProfit = max(maxProfit, price - minPrice)
            else:
                minPrice = price
                continue
            minPrice = min(minPrice, price)
        return maxProfit
        
