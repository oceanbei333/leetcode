#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        dp = [0]*l
        for i in range(l):
            if s[i] == ')':
                target = i - dp[i-1] - 1
                if target >= 0 and s[target] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        return max(dp) if dp else 0

    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        @functools.lru_cache(None)
        def dp(end: int) -> int:
            if end <= 0 or s[end] == '(':
                return 0
            length_pre = dp(end-1)
            target = end - length_pre - 1
            if target >= 0 and s[target] == '(':
                return length_pre + 2 + dp(end-length_pre-2)
            return 0
        return max(dp(i) for i in range(len(s)))


# @lc code=end
