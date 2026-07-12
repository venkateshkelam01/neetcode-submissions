class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)

        return max_profit

        # bruteforce
        # res = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sell  = prices[j]
        #         res = max(res, sell - buy)
        # return res