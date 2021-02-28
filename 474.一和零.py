#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
from typing import List


class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zero = [s.count('0') for s in strs]
        one = [s.count('1') for s in strs]

        @lru_cache(None)
        def dp(count: int, m: int, n: int):
            if count < 1:
                return 0
            res = dp(count-1, m, n)
            m -= zero[count-1]
            n -= one[count-1]
            if m >= 0 and n >= 0:
                res = max(res, dp(count-1, m, n)+1)
            return res
        return dp(len(strs), m, n)

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zero = [s.count('0') for s in strs]
        one = [s.count('1') for s in strs]
        l = len(strs)
        dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(l+1)]
        for i in range(1, l+1):
            for j in range(m+1):
                for k in range(n+1):
                    n_j = j - zero[i-1]
                    n_k = k - one[i-1]
                    if n_j >= 0 and n_k >= 0:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][n_j][n_k]+1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        return dp[l][m][n]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zero = [s.count('0') for s in strs]
        one = [s.count('1') for s in strs]
        l = len(strs)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, l+1):
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    n_j = j - zero[i-1]
                    n_k = k - one[i-1]
                    if n_j >= 0 and n_k >= 0:
                        dp[j][k] = max(dp[j][k], dp[n_j][n_k]+1)
                    else:
                        dp[j][k] = dp[j][k]
        return dp[m][n]
# @lc code=end
