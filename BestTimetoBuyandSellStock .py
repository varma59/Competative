class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        buy_point = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < buy_point:
                buy_point = prices[i]
            else:
                profit = prices[i] - buy_point
                max_profit = max(max_profit, profit)

        return max_profit
