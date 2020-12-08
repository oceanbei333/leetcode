#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return sum(val for val in range(1,num) if not num%val) == num
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        return sum( val+num//val for val in range(1, int( num**0.5)+1) if not num%val ) ==num *2
# @lc code=end

