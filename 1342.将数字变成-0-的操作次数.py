#
# @lc app=leetcode.cn id=1342 lang=python3
#
# [1342] 将数字变成 0 的操作次数
#

# @lc code=start
class Solution:
    def numberOfSteps (self, num: int) -> int:
        res = 0
        while num:
            if num%2:
                num -= 1
            else:
                num //=2
            res += 1
        return res
    def numberOfSteps (self, num: int) -> int:
        from itertools import count
        for ans in count():
            if not num:
                return ans
            num = num-1 if num%2 else num >> 1

# @lc code=end

