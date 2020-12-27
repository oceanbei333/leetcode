#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
from typing import List


class Solution:
    @lru_cache(None)
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        if len(s) == 1:
            return [[s]]
        res = []
        for i in range(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                for alist in self.partition(s[i+1:]):
                    res.append([s[:i+1]]+alist)
        return res

    def partition(self, s: str) -> List[List[str]]:
        from collections import defaultdict
        dp = defaultdict(list)
        flag = defaultdict(bool)
        dp[''] = [[]]
        n = len(s)

        def centerSpread(left, right):
            while 0 <= left and right < n and s[left] == s[right]:
                flag[(left, right)] = True
                left -= 1
                right += 1

        for i in range(n):
            centerSpread(i, i)
            centerSpread(i, i+1)

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if flag[(i, j)]:
                    for alist in dp[s[j+1:]]:
                        dp[s[i:]].append([s[i:j+1]]+alist)
        return dp[s]

# @lc code=end
