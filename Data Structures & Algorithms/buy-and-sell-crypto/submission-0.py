class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buyPrice = prices[0]
        sellPrice = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
                sellPrice = prices[i]
            if prices[i] > sellPrice:
                sellPrice = prices[i]
        return sellPrice - buyPrice