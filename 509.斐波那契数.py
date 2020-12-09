#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        @lru_cache(None)
        def _fib(n: int) -> int:
            if n in {0, 1}:
                return n
            return _fib(n-1) + _fib(n-2)
        return _fib(N)


class Solution:
    def fib(self, N: int) -> int:
        adict = {0: 0, 1: 1}
        for index in range(2, N+1):
            adict[index] = adict[index-1] + adict[index-2]
        return adict[N]


class Solution:
    def fib(self, N: int) -> int:
        if N in {0, 1}:
            return N
        pre1 = 1
        pre2 = 0
        for _ in range(2, N+1):
            val = pre1+pre2
            pre2 = pre1
            pre1 = val
        return val


class Solution:
    def fib(self, N: int) -> int:
        def _fib(level: int, n1: int, n2: int) -> int:
            if not level:
                return n1
            return _fib(level-1, n2, n1+n2)
        return _fib(N, 0, 1)

# @lc code=end
