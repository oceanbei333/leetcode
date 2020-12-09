#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        length = len(prices)

        def dfs(depth: int, count: int, is_has_stock: bool):
            if depth == length or count == 2:
                return 0
            profit_sell, profit_buy, profit_nothing = 0, 0, 0
            profit_nothing = dfs(depth+1, count, is_has_stock)
            if is_has_stock:
                profit_sell = dfs(depth+1, count+1, False) + prices[depth]
            else:
                profit_buy = dfs(depth+1, count, True) - prices[depth]
            return max(profit_sell, profit_buy, profit_nothing)
        return dfs(0, 0, False)

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        length = len(prices)

        @functools.lru_cache(None)
        def dfs(depth: int, count: int, is_has_stock: bool):
            if depth == length or count == 2:
                return 0
            profit_sell, profit_buy, profit_nothing = 0, 0, 0
            profit_nothing = dfs(depth+1, count, is_has_stock)
            if is_has_stock:
                profit_sell = dfs(depth+1, count+1, False) + prices[depth]
            else:
                profit_buy = dfs(depth+1, count, True) - prices[depth]
            return max(profit_sell, profit_buy, profit_nothing)
        return dfs(0, 0, False)

    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days < 2:
            return 0
        from collections import defaultdict
        dp = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        dp[0]['buy']['first'] = -prices[0]
        dp[0]['buy']['second'] = -prices[0]
        for day in range(1, days):
            # first buy
            dp[day]['buy']['first'] = max(
                dp[day-1]['buy']['first'], -prices[day])
            # first sell
            dp[day]['sell']['first'] = max(
                dp[day-1]['sell']['first'], dp[day-1]['buy']['first']+prices[day])
            # second buy
            dp[day]['buy']['second'] = max(
                dp[day-1]['buy']['second'], dp[day-1]['sell']['first']-prices[day])
            # second sell
            dp[day]['sell']['second'] = max(
                dp[day-1]['sell']['second'], dp[day-1]['buy']['second']+prices[day])

        return max(max(day_info['sell'].values()) for day_info in dp.values())

    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days < 2:
            return 0
        from collections import defaultdict
        dp = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        dp[0]['buy']['first'] = -prices[0]
        dp[0]['buy']['second'] = -prices[0]
        res = 0
        for day in range(1, days):
            # first buy
            dp[day]['buy']['first'] = max(
                dp[day-1]['buy']['first'], -prices[day])
            # first sell
            dp[day]['sell']['first'] = max(
                dp[day-1]['sell']['first'], dp[day-1]['buy']['first']+prices[day])
            # second buy
            dp[day]['buy']['second'] = max(
                dp[day-1]['buy']['second'], dp[day-1]['sell']['first']-prices[day])
            # second sell
            dp[day]['sell']['second'] = max(
                dp[day-1]['sell']['second'], dp[day-1]['buy']['second']+prices[day])
            res = max(res, *dp[day]['sell'].values())
        return res

    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days < 1:
            return 0
        dp = [([0, 0], [0, 0]) for _ in range(days)]
        dp[0][0][0] = -prices[0]
        dp[0][0][1] = -prices[0]
        res = 0
        for day in range(1, days):
            dp[day][0][0] = max(dp[day-1][0][0], -prices[day])
            dp[day][1][0] = max(dp[day-1][1][0], dp[day-1][0][0] + prices[day])
            dp[day][0][1] = max(dp[day-1][0][1], dp[day-1][1][0]-prices[day])
            dp[day][1][1] = max(dp[day-1][1][1], dp[day-1][0][1]+prices[day])
            res = max(res, dp[day][1][0], dp[day][1][1])
        return res

    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days < 2:
            return 0
        dp = [[0, 0, 0, 0] for _ in range(days)]
        dp[0][0] = -prices[0]
        dp[0][2] = -prices[0]
        res = 0
        for day in range(1, days):
            dp[day][0] = max(dp[day-1][0], -prices[day])
            dp[day][1] = max(dp[day-1][1], dp[day-1][0] + prices[day])
            dp[day][2] = max(dp[day-1][2], dp[day-1][1]-prices[day])
            dp[day][3] = max(dp[day-1][3], dp[day-1][2]+prices[day])
            res = max(res, dp[day][1], dp[day][3])
        return res

    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days < 2:
            return 0
        dp = [[0, 0, 0, 0] for _ in range(days)]
        dp[0][0] = -prices[0]
        dp[0][2] = -prices[0]
        res = 0
        for day in range(1, days):
            dp[day][0] = max(dp[day-1][0], -prices[day])
            dp[day][1] = max(dp[day-1][1], dp[day-1][0] + prices[day])
            dp[day][2] = max(dp[day-1][2], dp[day-1][1]-prices[day])
            dp[day][3] = max(dp[day-1][3], dp[day-1][2]+prices[day])
        return dp[-1][3]

    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days < 2:
            return 0
        first_buy, second_buy = -prices[0], -prices[0]
        first_sell, second_sell = 0, 0
        for day in range(1, days):
            first_buy = max(first_buy, -prices[day])
            first_sell = max(first_sell, first_buy+prices[day])
            second_buy = max(second_buy, first_sell-prices[day])
            second_sell = max(second_sell, second_buy+prices[day])
        return second_sell

    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days < 2:
            return 0
        first_buy, second_buy = -prices[0], -prices[0]
        first_sell, second_sell = 0, 0
        for price in prices[1:]:
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy+price)
            second_buy = max(second_buy, first_sell-price)
            second_sell = max(second_sell, second_buy+price)
        return second_sell

    def maxProfit(self, prices: List[int]) -> int:
        first_buy, second_buy = float('-inf'), float('-inf')
        first_sell, second_sell = 0, 0
        for price in prices:
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy+price)
            second_buy = max(second_buy, first_sell-price)
            second_sell = max(second_sell, second_buy+price)
        return second_sell

    def maxProfit(self, prices: List[int]) -> int:
        first_buy, second_buy = float('inf'), float('inf')
        first_sell, second_sell = 0, 0
        for price in prices:
            first_buy = min(first_buy, price)
            first_sell = max(first_sell, price-first_buy)
            second_buy = min(second_buy, price-first_sell)
            second_sell = max(second_sell, price-second_buy)
        return second_sell









# @lc code=end
