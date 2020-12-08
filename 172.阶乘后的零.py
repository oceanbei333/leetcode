#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
import functools


class Solution:
    def trailingZeroes(self, n: int) -> int:
        def func(n:int)->int:
            if n < 2:
                return 1
            return n*func(n-1)
        num = func(n)
        zero = 0
        while not num%10:
            zero += 1
            num //= 10
        return zero
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        while n > 0:
            n//=5
            zero_count += n
        return zero_count

# @lc code=end

