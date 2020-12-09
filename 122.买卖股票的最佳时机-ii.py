#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index in range(len(prices)-1):
            if prices[index+1] > prices[index]:
                profit += prices[index+1] - prices[index]
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        valley = peek = prices[0]
        index = 0
        length = len(prices)
        while index < length - 1:
            while index < length-1 and prices[index] >= prices[index+1]:
                index += 1
            valley = prices[index]
            while index < length-1 and prices[index] <= prices[index+1]:
                index += 1
            peek = prices[index]
            profit += peek - valley
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        return sum(prices[i+1] - prices[i] for i in range(len(prices)-1) if prices[i+1] > prices[i])

    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)

        def dfs(depth: int, hasing_stock: bool) -> int:
            if depth == length:
                return 0
            profit_sell, profit_buy, profit_nothing = 0, 0, 0
            profit_nothing = dfs(depth+1, hasing_stock)
            if hasing_stock:
                profit_sell = dfs(depth+1, False) + prices[depth]
            else:
                profit_buy = dfs(depth+1, True) - prices[depth]
            return max(profit_sell, profit_buy, profit_nothing)
        return dfs(0, False)

    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)

        @functools.lru_cache(None)
        def dfs(depth: int, hasing_stock: bool) -> int:
            if depth == length:
                return 0
            profit_sell, profit_buy, profit_nothing = 0, 0, 0
            profit_nothing = dfs(depth+1, hasing_stock)
            if hasing_stock:
                profit_sell = dfs(depth+1, False) + prices[depth]
            else:
                profit_buy = dfs(depth+1, True) - prices[depth]
            return max(profit_sell, profit_buy, profit_nothing)
        return dfs(0, False)

# @lc code=end
