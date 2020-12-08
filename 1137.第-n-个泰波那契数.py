#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
class Solution:
    @functools.lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if not n:
            return 0
        if n in {1,2}:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
    adict = dict()
    def tribonacci(self, n: int) -> int:
        if n in self.adict:
            return self.adict[n]
        if not n:
            return 0
        if n in {1,2}:
            return 1
        self.adict[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.adict[n]
        
    def tribonacci(self, n: int) -> int:
        def func(n:int, n1:int=1, n2:int=1, n3:int=0):
            if not n:
                return 0
            if n in {1,2}:
                return 1
            return func(n-1, n1+n2+n3, n1, n2)
        return func(n, 1, 1, 0)

# @lc code=end

