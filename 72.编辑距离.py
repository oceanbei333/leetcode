#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if not m*n:
            return m+n
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    continue
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        @functools.lru_cache(None)
        def dp(i: int, j: int) -> int:
            if not i*j:
                return i+j
            if word1[i-1] == word2[j-1]:
                return dp(i-1, j-1)
            return min(dp(i-1, j-1), dp(i, j-1), dp(i-1, j))+1
        return dp(len(word1), len(word2))

# @lc code=end
