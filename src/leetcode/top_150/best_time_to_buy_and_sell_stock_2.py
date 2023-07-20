from typing import List


class BestTimeToBuyAndSellStock2:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for index in range(1, len(prices)):
            if prices[index - 1] < prices[index]:
                total_profit += prices[index] - prices[index - 1]
        return total_profit
