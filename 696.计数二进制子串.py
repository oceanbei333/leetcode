#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s)<2:
            return 0
        pre=0
        cur = 1
        res = 0
        for index in range(1, len(s)):
            if s[index] == s[index-1]:
                cur += 1
            else:
                res += min(pre, cur)
                pre = cur
                cur = 1
        return res + min(pre, cur)


        
# @lc code=end

