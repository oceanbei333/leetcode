#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
import functools


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = list(range(1, n+1))
        for i in range(2, n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        cur, next_, = 1, 2
        for _ in range(2, n):
            cur, next_ = next_, cur+next_
        return next_

    def climbStairs(self, n: int) -> int:
        @functools.lru_cache
        def helper(n: int):
            if n in {1, 2}:
                return n
            return helper(n-1)+helper(n-2)
        return helper(n)

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        def helper(cur: int, next: int, n: int):
            if n == 2:
                return next
            return helper(next, cur+next, n-1)
        return helper(1, 2, n)


# @lc code=end
