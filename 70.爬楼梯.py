#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
import functools


class Solution:
    @functools.lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n in {1, 2}:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs(self, n: int) -> int:
        def _climbStairs(n: int, cur: int, pre: int):
            if n == 1:
                return pre
            if n == 2:
                return cur
            return _climbStairs(n-1, cur+pre, cur)
        return _climbStairs(n, 2, 1)

    def climbStairs(self, n: int) -> int:
        if n in {1, 2}:
            return n
        cue, next_, = 1, 2
        for _ in range(2, n):
            cue, next_ = next_, cue+next_
        return next_

    def climbStairs(self, n: int) -> int:
        dp = list(range(1, n+1))
        for i in range(2, n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n-1]


# @lc code=end
