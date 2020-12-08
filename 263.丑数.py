#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if not num:
            return False
        while num !=1:
            if not num%2:
                num //=2
            elif not num%3:
                num //=3
            elif not num%5:
                num //=5
            else:
                break
        return num == 1
    def isUgly(self, num: int) -> bool:
        if not num:
            return False
        while not num%2:
            num //= 2
        while not num%3:
            num //= 3
        while not num%5:
            num //= 5
        return num == 1
# @lc code=end

