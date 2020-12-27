#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        return bool(re.match(f"^{p}$", s))

    def isMatch(self, s: str, p: str) -> bool:
        l_s, l_p = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if not i or not j:
                return False
            return p[j-1] in {'.', s[i-1]}

        # dp[0][0]都是空字符串,
        dp = [[False] * (l_p + 1) for _ in range(l_s + 1)]
        dp[0][0] = True
        # s从空字符串开始匹配
        for i in range(l_s + 1):
            # p从第一个字符串开始匹配
            for j in range(1, l_p + 1):
                if j and p[j - 1] == '*':
                    # j 可能取到-1
                    dp[i][j] = dp[i][j - 2]
                    if matches(i, j - 1):
                        # i >0 , 所有i-1取不到 -1
                        dp[i][j] |= dp[i - 1][j]
                elif matches(i, j):
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[l_s][l_p]

    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        return first_match and self.isMatch(s[1:], p[1:])

# @lc code=end
