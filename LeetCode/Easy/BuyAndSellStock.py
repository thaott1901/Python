class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = inf
        for i in range(len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            else:
                profit = max(profit, prices[i] - minPrice)
        return profit