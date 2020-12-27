#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] != s[r]:
                s1 = s[l:r]
                s2 = s[l+1:r+1]
                return s1 == s1[::-1] or s2 == s2[::-1]
            else:
                l += 1
                r -= 1
        return True


# @lc code=end
