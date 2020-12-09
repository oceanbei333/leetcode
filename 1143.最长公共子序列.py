#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @functools.lru_cache(None)
        def dp(i:int,j:int)->int:
            if i <0 or j<0:
                return 0
            if text1[i] == text2[j]:
                return dp(i-1, j-1)+1
            else:
                return max(dp(i-1, j), dp(i, j-1))
        return dp(len(text1)-1, len(text2)-1)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1)+1, len(text2)+1
        table = [[0]*(m) for _ in range(n) ]
        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    table[j][i] = 1+ table[j-1][i-1]
                else:
                    table[j][i] = max(table[j-1][i], table[j][i-1])
        return table[-1][-1]
# @lc code=end

