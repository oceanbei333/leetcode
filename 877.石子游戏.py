#
# @lc app=leetcode.cn id=877 lang=python3
#
# [877] 石子游戏
#

# @lc code=start
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(len(piles)**2)
        def dp(left: int, right: int):
            if left > right:
                return 0
            return max(piles[left] - dp(left+1, right), piles[right]-dp(left, right-1))
        return dp(0, len(piles)-1) > 0

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for left in range(n):
            for length in range(1, n-left+1):
                right = left + length - 1
                dp[left][right] = max(
                    piles[left]-dp[left+1][right], piles[right]-dp[left][right-1])
        return dp[0][n-1] > 0

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for left in range(n):
            for length in range(1, n-left+1):
                right = left + length - 1
                dp[left][right] = max(
                    piles[left]-dp[left+1][right], piles[right]-dp[left][right-1])
        return dp[0][n-1] > 0

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i, pile in enumerate(piles):
            dp[i][i] = pile
        for left in range(n - 2, -1, -1):
            for right in range(left + 1, n):
                dp[left][right] = max(piles[left] - dp[left + 1][right],
                                      piles[right] - dp[left][right - 1])
        return dp[0][n - 1] > 0

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [0] * n
        for i, pile in enumerate(piles):
            dp[i] = pile
        for left in range(n - 2, -1, -1):
            for right in range(left + 1, n):
                dp[right] = max(piles[left] - dp[right],
                                piles[right] - dp[right - 1])
        return dp[n - 1] > 0
    def stoneGame(self, piles: List[int]) -> bool:
        return True

# @lc code=end
