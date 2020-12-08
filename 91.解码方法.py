#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s and s[0] == '0':
            return 0
        n = len(s)

        @functools.lru_cache(n)
        def dp(end: int) -> int:
            if end < 0:
                return 1
            res = 0
            if 1 <= int(s[end]) <= 9:
                res += dp(end-1)
            if end > 0 and 10 <= int(s[end-1:end+1]) <= 26:
                res += dp(end-2)
            return res
        return dp(n-1)

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        s += '0'
        dp[-1] = 1
        for i in range(n):
            if 1 <= int(s[i]) <= 9:
                dp[i] = dp[i-1]
            if 10 <= int(s[i-1]+s[i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-2]

    def numDecodings(self, s: str) -> int:
        n = len(s)
        cur, pre, pre_pre = 0, 1, 1
        s = '0'+s
        for i in range(n):
            cur = 0
            if 1 <= int(s[i+1]) <= 9:
                cur = pre
            if 10 <= int(s[i:i+2]) <= 26:
                cur += pre_pre
            pre, pre_pre = cur, pre
        return cur


# @lc code=end
