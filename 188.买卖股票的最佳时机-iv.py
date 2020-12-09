#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)

        @functools.lru_cache(None)
        def _maxProfit(date: int, count: int, hasing_stock: bool) -> int:
            if date >= days or count >= k:
                return 0
            # do nothing
            profit_nothing = profit_sell = profit_buy = _maxProfit(
                date+1, count, hasing_stock)
            if hasing_stock:
                profit_sell = _maxProfit(date+1, count+1, False) + prices[date]
            else:
                profit_buy = _maxProfit(date+1, count, True) - prices[date]
            return max(profit_nothing, profit_buy, profit_sell)
        return _maxProfit(0, 0, False)

    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
        if days < 2 or not k:
            return 0
        from collections import defaultdict
        dp = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        for i in range(-1, k):
            dp[0][i]['hasing_stock'] = -prices[0]
        for date in range(1, days):
            for trade in range(k):
                dp[date][trade]['hasing_stock'] = max(
                    dp[date-1][trade]['hasing_stock'], dp[date-1][trade-1]['no_stock']-prices[date])
                dp[date][trade]['no_stock'] = max(
                    dp[date-1][trade]['no_stock'], dp[date-1][trade]['hasing_stock']+prices[date])
        return max(item['no_stock'] for item in dp[days-1].values())

    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
        if days < 2 or not k:
            return 0
        dp = [[[0, 0] for _ in range(k+1)] for _ in range(days)]
        for i in range(k):
            dp[0][i][0] = -prices[0]
        for date in range(1, days):
            for trade in range(k):
                dp[date][trade][0] = max(
                    dp[date-1][trade][0], dp[date-1][trade-1][1]-prices[date])
                dp[date][trade][1] = max(
                    dp[date-1][trade][1], dp[date-1][trade][0]+prices[date])
        return max(item[1] for item in dp[-1])

    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
        if days < 2 or not k:
            return 0
        hasing_stocks = [-prices[0] for _ in range(k)]
        no_stocks = [0 for _ in range(k+1)]
        for date in range(1, days):
            for trade in range(k):
                hasing_stocks[trade], no_stocks[trade] = (
                    max(hasing_stocks[trade], no_stocks[trade-1]-prices[date]),
                    max(no_stocks[trade], hasing_stocks[trade]+prices[date])
                )
        return no_stocks[-2]
# @lc code=end
