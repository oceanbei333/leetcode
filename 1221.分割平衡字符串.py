#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        res = 0
        for index in range(len(s)):
            count += 1 if s[index] == 'L' else -1
            if index and not count:
                res += 1
        return res

        
        
# @lc code=end

