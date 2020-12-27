#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if not s:
            return set(p) == {'*'}
        if p[0] == '*':
            return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
        if p[0] in {s[0], '?'}:
            return self.isMatch(s[1:], p[1:])
        return False

    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        for i in range(len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] | dp[i-1][j]
                elif i and p[j-1] in {s[i-1], '?'}:
                    dp[i][j] = dp[i-1][j-1]
        return dp[len(s)][len(p)]

    def isMatch(self, s: str, p: str) -> bool:
        dp = [False]*(len(p)+1)
        dp[0] = True
        for i in range(len(s)+1):
            pre = dp[0]
            if i:
                dp[0] = False
            for j in range(1, len(p)+1):
                cur = dp[j]
                if p[j-1] == '*':
                    dp[j] |= dp[j-1]
                elif i and p[j-1] in {s[i-1], '?'}:
                    dp[j] = pre
                else:
                    dp[j] = False
                pre = cur
        return dp[-1]


# @lc code=end
