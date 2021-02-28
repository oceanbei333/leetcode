#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        return [bin(i).count('1') for i in range(num+1)]

    def countBits(self, num: int) -> List[int]:
        @lru_cache(num+1)
        def dp(num: int):
            if not num:
                return 0
            if num == 1:
                return 1
            if num % 2:
                return dp((num-1) >> 1)+1
            return dp(num >> 1)
        return [dp(i) for i in range(num+1)]

    def countBits(self, num: int) -> List[int]:
        dp = [0]*(num+1)
        for i in range((num >> 1)+1):
            dp[i*2] = dp[i]
            if i*2+1 <= num:
                dp[i*2+1] = dp[i]+1
        return dp

    def countBits(self, num: int) -> List[int]:
        @lru_cache(num+1)
        def dp(num: int):
            if not num:
                return 0
            return dp(num & (num-1)) + 1
        return [dp(i) for i in range(num+1)]

    def countBits(self, num: int) -> List[int]:
        dp = [0]*(num+1)
        for i in range(1, num+1):
            dp[i] = dp[i & (i-1)]+1
        return dp


# @lc code=end
