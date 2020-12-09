#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        @functools.lru_cache(None)
        def dp(end: int) -> int:
            count = 0
            if int(s[end]):
                if not end:
                    return 1
                count = dp(end-1)
            if end >= 1 and 9 < int(s[end-1:end+1]) <= 26:
                if end == 1:
                    return count + 1
                count += dp(end-2)
            return count
        return dp(len(s)-1)

    def numDecodings(self, s: str) -> int:
        l = len(s)
        dp = [0]*(l+1)
        dp[0] = 1 if int(s[0]) else 0
        dp[-1] = 1
        for i in range(1, l):
            if int(s[i]):
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
        return dp[-2]

    def numDecodings(self, s: str) -> int:
        l = len(s)
        pre = 1 if int(s[0]) else 0
        pre_pre = 1
        for i in range(1, l):
            cur = 0
            if int(s[i]):
                cur += pre
            if 10 <= int(s[i-1: i+1]) <= 26:
                cur += pre_pre
            pre, pre_pre = cur, pre
        return pre


# @lc code=end
