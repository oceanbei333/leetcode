#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        dp = [[False]*n for _ in range(n)]
        for length in range(1, n+1):
            for start in range(n):
                end = start+length-1
                if end >= n:
                    break
                if length == 1:
                    dp[start][end] = True
                elif length == 2 or dp[start+1][end-1]:
                    dp[start][end] = s[start] == s[end]
                if dp[start][end] and length > len(res):
                    res = s[start:end+1]
        return res

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.res = ''
        s += '#*'

        def check(l: int, r: int):
            while s[l] == s[r]:
                if r-l+1 > len(self.res):
                    self.res = s[l:r+1]
                l -= 1
                r += 1

        for mid in range(n):
            check(mid, mid)
            check(mid, mid+1)
        return self.res


# @lc code=end
