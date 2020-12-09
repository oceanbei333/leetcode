#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
    def myPow(self, x: float, n: int) -> float:
        def _myPow(x:float, n:int)-> float:
            if not n:
                return 1
            return _myPow(x, n-1)*x

        if n >0:
            return _myPow(x, n)
        else:
            return 1/_myPow(x, -n)

    def myPow(self, x: float, n: int) -> float:
        res = 1
        for _ in range(abs(n)):
            res *= x
        if n<0:
            res = 1/res
        return res
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        from functools import reduce
        alist = [x]*abs(n)
        res = reduce(lambda x,y: x*y, alist)
        if n<0:
            res = 1/res
        return res
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        from functools import reduce
        res = reduce(lambda m,n: x*m, range(1,abs(n)+2))
        if n<0:
            res = 1/res
        return res
    def myPow(self, x: float, n: int) -> float:
        def _myPow(x:float, n:int)->float:
            if not n:
                return 1
            return _myPow(x*x, n//2)*(x if n%2 else 1)
        res =  _myPow(x, abs(n))
        return res if n>0 else 1/res
    def myPow(self, x: float, n: int) -> float:
        from functools import lru_cache
        @lru_cache(None)
        def _myPow(x:float, n:int)-> float:
            if not n:
                return 1
            return _myPow(x, n//2)*_myPow(x, n//2)*(x if n%2 else 1)

        if n >0:
            return _myPow(x, n)
        else:
            return 1/_myPow(x, -n)

# @lc code=end

