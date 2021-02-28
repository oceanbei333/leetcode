#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dp(start: int, end: int):
            if start > end:
                return 0
            if start == end:
                return 1
            if s[start] == s[end]:
                return dp(start+1, end-1) + 2
            return max(dp(start+1, end), dp(start, end-1))
        return dp(0, len(s)-1)

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for end in range(1, n):
            for start in range(end-1, -1, -1):
                if s[start] == s[end]:
                    dp[start][end] = dp[start+1][end-1] + 2
                else:
                    dp[start][end] = max(dp[start+1][end], dp[start][end-1])
        return dp[0][n-1]

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [1]*n
        for end in range(n):
            pre = 0
            for start in range(end-1, -1, -1):
                temp = dp[start]
                if s[start] == s[end]:
                    dp[start] = pre + 2
                else:
                    dp[start] = max(dp[start+1], dp[start])
                pre = temp
        return dp[0]

# @lc code=end
