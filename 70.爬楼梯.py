#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
from functools import lru_cache


class Solution:
    @functools.lru_cache
    def climbStairs(self, n: int) -> int:
        if n in (1, 2):
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs(self, n: int) -> int:
        result = {1: 1, 2: 2}
        for i in range(3, n+1):
            result[i] = result[i-1] + result[i-2]
        return result[n]

    def climbStairs(self, n: int) -> int:
        if n in (1, 2):
            return n
        a, b, = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b

    def climbStairs(self, n: int) -> int:
        def _climbStairs(level: int, n1:int, n2:int):
            if level == 1:
                return n2
            if level == 2:
                return n1
            return _climbStairs(level-1, n1+n2, n1)
        return _climbStairs(n,2, 1)



# @lc code=end
