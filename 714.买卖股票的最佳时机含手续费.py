#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        days = len(prices)
        @functools.lru_cache(None)
        def _maxProfit(date:int, hasing_stock:bool):
            if date >= days:
                return 0
            profit_nothing = profit_sell =  profit_buy = _maxProfit(date+1, hasing_stock)
            if hasing_stock:
                profit_sell = _maxProfit(date+1, False) + prices[date] - fee
            else:
                profit_buy = _maxProfit(date+1, True) - prices[date]
            return max(profit_nothing, profit_sell, profit_buy)
        return _maxProfit(0, False)
    def maxProfit(self, prices: List[int], fee: int) -> int:
        days = len(prices)
        if days < 2:
            return 0
        from collections import defaultdict
        dp = defaultdict(lambda:defaultdict(int))
        dp[0]['hasing_stock'] = -prices[0]
        for date in range(1, days):
            dp[date]['hasing_stock'] = max(dp[date-1]['hasing_stock'], dp[date-1]['no_stock']-prices[date])
            dp[date]['no_stock'] = max(dp[date-1]['no_stock'], dp[date-1]['hasing_stock']+prices[date]-fee)
        return dp[days-1]['no_stock']
    def maxProfit(self, prices: List[int], fee: int) -> int:
        days = len(prices)
        if days < 2:
            return 0
        dp = [[0,0] for _ in range(days)]
        dp[0][0] = -prices[0]
        for date in range(1,days):
            dp[date][0] = max(dp[date-1][0], dp[date-1][1]-prices[date])
            dp[date][1] = max(dp[date-1][1], dp[date-1][0]+prices[date]-fee)
        return dp[-1][1]
    def maxProfit(self, prices: List[int], fee: int) -> int:
        days = len(prices)
        if days < 2:
            return 0
        has_stock = -prices[0]
        no_stock = 0
        for date in range(1, days):
            has_stock, no_stock = max(has_stock, no_stock-prices[date]), max(no_stock, has_stock+prices[date]-fee)
        return no_stock
# @lc code=end

