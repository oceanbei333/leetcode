#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
from typing import List, Union


class Solution:
    def coinChange(self, coins: List[int], amount: int):
        n = len(coins)

        @lru_cache(None)
        def dp(count: int, target: int):
            if not target:
                return 0
            if count < 1 or target < 0:
                return amount + 1
            return min(dp(count-1, target), dp(count, target-coins[count-1])+1)
        res = dp(n, amount)
        return res if res < amount+1 else -1

    def coinChange(self, coins: List[int], amount: int):
        n = len(coins)
        MAX_AMOUNT = amount + 1
        dp = [[MAX_AMOUNT]*(MAX_AMOUNT) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for i in range(1, n+1):
            for target in range(MAX_AMOUNT):
                if target >= coins[i-1]:
                    dp[i][target] = min(
                        dp[i-1][target], dp[i][target-coins[i-1]]+1)
                else:
                    dp[i][target] = dp[i-1][target]
        return dp[n][amount] if dp[n][amount] < MAX_AMOUNT else -1

    def coinChange(self, coins: List[int], amount: int):
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for target in range(coin, amount+1):
                dp[target] = min(dp[target], dp[target-coin]+1)
        return -1 if dp[amount] == amount+1 else dp[amount]

    def coinChange(self, coins: List[int], amount: int):
        @lru_cache(None)
        def dp(target: int):
            if not target:
                return 0
            if target < 0:
                return float('inf')
            return min(dp(target-coin)+1 for coin in coins)
        return dp(amount) if dp(amount) < float('inf') else -1


# @lc code=end
