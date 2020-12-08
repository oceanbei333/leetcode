#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            val =  int(''.join( str(x)[::-1] ))
        else:
            val = -int(''.join( str(-x)[::-1] ))
        if val < -2**31 or val > 2**31-1:
            return 0
        else:
            return val
    def reverse(self, x: int) -> int:
        boundry = 1<<31 if x < 0 else  (1<<31)-1
        y = abs(x)
        res = 0
        while y:
           res = res*10 + y%10
           y //= 10
           if res > boundry:
               return 0
        return res if x>0 else -res
# @lc code=end

