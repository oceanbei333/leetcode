#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        s += '#*'

        def check(l: int, r: int, res):
            while s[l] == s[r]:
                if r-l+1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
            return res

        res = ''
        for mid in range(n):
            res = check(mid, mid, res)
            res = check(mid, mid+1, res)
        return res

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        left = right = 0
        dp = [[False]*n for _ in range(n)]
        for start in range(n-1, -1, -1):
            for end in range(start, n):
                length = end-start+1
                if length == 1:
                    dp[start][end] = True
                elif length == 2 or dp[start+1][end-1]:
                    dp[start][end] = s[start] == s[end]
                if dp[start][end] and length > right-left+1:
                    left, right = start, end
        return s[left:right+1]

# @lc code=end
