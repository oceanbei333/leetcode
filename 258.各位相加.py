#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        astr = str(num)
        if len(astr) == 1:
            return num
        return self.addDigits( sum(int(s) for s in astr) )
    def addDigits(self, num: int) -> int:
        astr = str(num)
        while len(astr) !=1:
            astr = str(sum(int(s) for s in astr))
        return int(astr)
    def addDigits(self, num: int) -> int:
        if not num:
            return num
        return ((num-1) % 9) + 1


# @lc code=end

