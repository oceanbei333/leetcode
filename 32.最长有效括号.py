#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)

        @functools.lru_cache(n)
        def dp(end: int) -> int:
            if end < 1 or s[end] == '(':
                return 0
            if s[end-1] == '(':
                return dp(end-2) + 2
            if s[end-1] == ')':
                index = end-dp(end-1)-1
                if index >= 0 and s[index] == '(':
                    return dp(end-1) + dp(end-dp(end-1)-2) + 2
            return 0
        return max(dp(i) for i in range(n))

    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        s += '#'
        for i in range(n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1]+dp[i-dp[i-1]-2] + 2
        return max(dp)

    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        n, res = len(s), 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i-stack[-1])
                else:
                    stack.append(i)
        return res

    def longestValidParentheses(self, s: str) -> int:
        l, r, res = 0, 0, 0
        for c in s:
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                res = max(res, l*2)
            elif r > l:
                l, r = 0, 0

        l, r = 0, 0
        for c in s[::-1]:
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                res = max(res, l*2)
            elif r < l:
                l, r = 0, 0

        return res


# @lc code=end
