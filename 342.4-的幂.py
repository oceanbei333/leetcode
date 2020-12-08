#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if not num:
           return False
        while not num%4:
            num //=4
        return num ==1
# @lc code=end

