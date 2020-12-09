#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days < 2:
            return 0

        @functools.lru_cache(None)
        def _maxProfit(day: int, sell_day: int) -> int:
            if day == days:
                return 0
            profit_nothing = profit_sell = profit_buy = _maxProfit(
                day+1, sell_day)
            if sell_day and day - sell_day > 1:
                profit_buy = _maxProfit(day+1, 0) - prices[day]
            if not sell_day:
                profit_sell = _maxProfit(day+1, day) + prices[day]
            return max(profit_nothing, profit_buy, profit_sell)
        return _maxProfit(0, -2)

    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days < 2:
            return 0
        from collections import defaultdict
        dp = defaultdict(lambda: defaultdict(int))
        dp[0]['with_stock'] = -prices[0]
        for day in range(1, days):
            dp[day]['with_stock'] = max(
                dp[day-1]['with_stock'], dp[day-1]['unfreeze']-prices[day])
            dp[day]['freeze'] = dp[day-1]['with_stock']+prices[day]
            dp[day]['unfreeze'] = max(
                dp[day-1]['unfreeze'], dp[day-1]['freeze'])
        print(dict(**dp))
        return max(dp[days-1].values())

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        dp = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        for day in range(1, n):
            dp[day][0] = max(dp[day - 1][0], dp[day - 1][2] - prices[day])
            dp[day][1] = dp[day - 1][0] + prices[day]
            dp[day][2] = max(dp[day - 1][1], dp[day - 1][2])
        print(dp)
        return max(dp[n - 1][1], dp[n - 1][2])

    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days < 2:
            return 0
        dp = [[0, 0, 0] for _ in range(days)]
        dp[0][0] = -prices[0]
        for day in range(1, days):
            dp[day][0] = max(dp[day-1][0], dp[day-1][2]-prices[day])
            dp[day][1] = dp[day-1][0] + prices[day]
            dp[day][2] = max(dp[day-1][1], dp[day-1][2])
        return max(dp[-1])

    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days < 2:
            return 0
        with_stock = -prices[0]
        freeze, unfreeze = 0, 0
        for price in prices[1:]:
            with_stock, freeze, unfreeze = max(
                with_stock, unfreeze-price), with_stock + price, max(unfreeze, freeze)
        return max(freeze, unfreeze)


# @lc code=end
