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

# @lc code=end
