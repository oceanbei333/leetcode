#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)

        @lru_cache(len(s))
        def dp(i: int):
            if not i:
                return True
            return any(s[j:i] in wordset and dp(j) for j in range(i))
        return dp(len(s))


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1,n+1):
            dp[i] = any(s[j:i] in wordset and dp[j] for j in range(i))
        return dp[n]
# @lc code=end
