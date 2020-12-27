#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        index = 1
        res = ''
        s = '-'+s
        while index < len(s):
            res += s[index+k-1:index-1:-1]+s[index+k: index+2*k]
            index += 2*k
        return res

    def reverseStr(self, s: str, k: int) -> str:
        alist = list(s)
        for i in range(0, len(alist), 2*k):
            alist[i:i+k] = reversed(alist[i:i+k])
        return ''.join(alist)

    def reverseStr(self, s: str, k: int) -> str:
        return ''.join(s[i:i+k][::-1]+s[i+k:i+2*k] for i in range(0, len(s), 2*k))

# @lc code=end
