from typing import List


class BestTimeToBuyAndSellStock:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit = 0
        for index in range(1, len(prices)):
            max_profit = max(max_profit, prices[index] - min_so_far)
            min_so_far = min(min_so_far, prices[index])
        return max_profit