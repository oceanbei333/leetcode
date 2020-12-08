#
# @lc app=leetcode.cn id=1323 lang=python3
#
# [1323] 6 和 9 组成的最大数字
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        for index in range(len(s)):
            if s[index] == "6":
                return num + 10**(len(s)-index-1)*3
        return num
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
        
# @lc code=end

