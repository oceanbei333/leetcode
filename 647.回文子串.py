#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_vaild(s: str):
            return s == s[::-1]
        length = len(s)
        res = 0
        for i in range(length):
            for j in range(i+1, length+1):
                if is_vaild(s[i:j]):
                    res += 1
        return res

    def countSubstrings(self, s: str) -> int:
        length = len(s)
        res = 0

        def check(l: int, r: int) -> int:
            res = 0
            while l >= 0 and r <= length-1 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        for i in range(length):
            res += check(i, i)
            res += check(i, i+1)
        return res
# @lc code=end
