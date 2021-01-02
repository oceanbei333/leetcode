#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return list(combinations(range(1, n+1), k))

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = list(range(1, k+1)) + [n+1]
        j = 0
        while j < k:
            res.append(temp[:k])
            j = 0
            # 从后固定值，前面以等差数列的形式追赶
            while j < k and temp[j] + 1 == temp[j+1]:
                temp[j] = j+1
                j += 1
            temp[j] += 1
        return res

    def combine(self, n: int, k: int) -> List[List[int]]:
        def dp(n: int, k: int):
            if not k:
                return [[]]
            if n < 1 or k < 0:
                return []
            res = dp(n-1, k)
            for item in dp(n-1, k-1):
                res.append(item+[n])
            return res
        return dp(n, k)

    def combine(self, n: int, k: int) -> List[List[int]]:
        dp = [[[] for _ in range(k+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0].append([])
        for i in range(1, n+1):
            for j in range(1, k+1):
                for item in dp[i-1][j]:
                    dp[i][j].append(item[:])
                for item in dp[i-1][j-1]:
                    dp[i][j].append(item+[i])
        return dp[n][k]

    def combine(self, n: int, k: int) -> List[List[int]]:
        dp = [[] for _ in range(k+1)]
        dp[0].append([])
        for i in range(1, n+1):
            for j in range(k, 0, -1):
                for item in dp[j-1]:
                    dp[j].append(item+[i])
        return dp[k]
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(used: List[int], first: int):
            if len(used)==k:
                res.append(used)
                return
            for num in range(first, n+1):
                helper(used+[num], num+1)
        helper([], 1)
        return res

# @lc code=end
