#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# @lc code=start
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()
    def toLowerCase(self, str: str) -> str:
        res = ''
        for s in str:
            if  ord('A') <= ord(s) <= ord('Z'):
                res += chr(ord(s)+32)
            else:
                res += s
        return res

        
# @lc code=end

