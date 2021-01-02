#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s
        prefix = ''
        i = 0
        while i < len(s) and not s[i].isnumeric():
            prefix += s[i]
            i += 1
        if i < len(s):
            count = int(s[i])
            return prefix + self.decodeString(s[i+1:len(s)-2])*count
        return prefix

    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ''
        next_multi = 0
        n = len(s)
        for i in range(n):
            if s[i].isnumeric():
                next_multi = next_multi*10 + int(s[i])
            elif s[i].isalpha():
                cur_str += s[i]
            elif s[i] == '[':
                stack.append((cur_str, next_multi))
                cur_str = ''
                next_multi = 0
            else:
                pre_str, cur_multi = stack.pop()
                cur_str *= cur_multi
                cur_str = pre_str + cur_str
        return cur_str

# @lc code=end
