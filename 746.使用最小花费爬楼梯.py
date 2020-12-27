#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache
        def _generate(n: int) -> int:
            if n in {0, 1}:
                return cost[n]
            return cost[n] + min(_generate(n-1), _generate((n-2)))
        return min(_generate(len(cost)-1), _generate(len(cost)-2))

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache
        def _generate(n: int) -> int:
            if n < 2:
                return 0
            return min(cost[n-1]+_generate(n-1), cost[n-2]+_generate(n-2))
        return _generate(len(cost))

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        dp = [0]*(l+1)
        for i in range(2, l+1):
            dp[i] = min(cost[i-1]+dp[i-1], cost[i-2]+dp[i-2])
        return dp[l]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cur, pre = 0, 0
        for i in range(2, len(cost)+1):
            cur, pre = min(cost[i-1]+cur, cost[i-2]+pre), cur
        return cur


# @lc code=end
