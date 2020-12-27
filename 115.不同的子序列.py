#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @functools.lru_cache(None)
        def dp(s_index: int, t_index: int):
            if t_index < 0:
                return 1
            if s_index < 0:
                return 0
            if s[s_index] == t[t_index]:
                return dp(s_index-1, t_index-1) + dp(s_index-1, t_index)
            return dp(s_index-1, t_index)
        return dp(len(s)-1, len(t)-1)

    def numDistinct(self, s: str, t: str) -> int:
        len_s = len(s)
        len_t = len(t)
        dp = [[0]*(len_t+1) for _ in range(len_s+1)]
        for i in range(len_s+1):
            dp[i][-1] = 1
        for s_index in range(len_s):
            for t_index in range(len_t):
                if s[s_index] == t[t_index]:
                    dp[s_index][t_index] += dp[s_index-1][t_index-1]
                dp[s_index][t_index] += dp[s_index-1][t_index]
        return dp[len_s-1][len_t-1]

    def numDistinct(self, s: str, t: str) -> int:
        dp = [0]*len(t)
        for s_index in range(len(s)):
            pre = 1
            for t_index in range(len(t)):
                cur = dp[t_index]
                if s[s_index] == t[t_index]:
                    dp[t_index] += pre
                pre = cur
        return dp[len(t)-1]

# @lc code=end
