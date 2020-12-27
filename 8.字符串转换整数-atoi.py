#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')
        nums = set(map(str, range(10)))
        if not s or s[0] not in nums | {'-', '+'}:
            return 0
        first = s[0]
        if first in {'-', '+'}:
            s = s[1:]
        num = 0
        for c in s:
            if c in nums:
                num *= 10
                num += int(c)
            else:
                break
        if first == '-':
            num = -num
        return max(-1<<31, min(num, (1<<31)-1))

# @lc code=end
