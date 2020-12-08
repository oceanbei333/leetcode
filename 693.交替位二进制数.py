#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)[2:]
        for index in range(len(s)-1):
            if s[index] == s[index+1]:
                return False
        return True

# @lc code=end

