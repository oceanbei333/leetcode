#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dp(i-1, j-1)+1
            return max(dp(i-1, j), dp(i, j-1))
        return dp(len(text1)-1, len(text2)-1)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        for x in range(l1):
            for y in range(l2):
                if text1[x] == text2[y]:
                    dp[x][y] = dp[x-1][y-1] + 1
                else:
                    dp[x][y] = max(dp[x][y-1], dp[x-1][y])
        return dp[l1-1][l2-1]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [0]*(l2+1)
        for i in range(l1):
            pre = 0
            for j in range(l2):
                cur = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = pre+1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                pre = cur
        return dp[l2-1]


# @lc code=end
