#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dp(count:int, target):
            if not target:
                return 1
            if count<1 or  target < 0:
                return 0
            return dp(count-1, target) + dp(count, target-coins[count-1])
        return dp(len(coins), amount)

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        for i in range(0, n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for target in range(1, amount+1):
                if target - coins[i-1]< 0:
                    dp[i][target] = dp[i-1][target]
                else:
                    dp[i][target] = dp[i-1][target] + dp[i][target-coins[i-1]]
        return dp[n][amount]

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for target in range(coin, amount+1):
                dp[target] += dp[target-coin]
        return dp[amount]

          

# @lc code=end
