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
        return ''.join(chr(ord(s)+32) if ord('A') <= ord(s) <= ord('Z') else s for s in str)

# @lc code=end
