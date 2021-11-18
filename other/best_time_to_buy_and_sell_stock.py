# 121 https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

class Solution:
    """
    Runtime: 984 ms, faster than 80.64% of Python3 online submissions for Best Time to Buy and Sell Stock.
    Memory Usage: 25.2 MB, less than 11.62% of Python3 online submissions for Best Time to Buy and Sell Stock.
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low = prices[0]
        for x in prices[1:]:
            if low < x:
                max_profit = max(max_profit, x - low)
            elif x < low:
                low = x

        return max_profit