#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return '0'
        res = ''
        val = abs(num)
        while val:
            res = str(val%7) + res
            val //= 7
        return res if num>=0 else '-' + res
        
# @lc code=end

