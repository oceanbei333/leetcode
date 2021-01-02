#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        res = []

        def helper(index: int, used: List[int], target: int):
            if not target:
                if len(used) == k:
                    res.append(used)
                return
            if index < 0 or target < 0 or len(used) > k:
                return
            helper(index-1, used, target)
            helper(index-1, used+[nums[index]], target-nums[index])
        helper(8, [], n)
        return res

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dp(num: int, target: int):
            if not target:
                return [[]]
            if num < 1 or target < 0:
                return []
            res = dp(num-1, target)
            for item in dp(num-1, target-num):
                res.append(item+[num])
            return res
        return [item for item in dp(9, n) if len(item) == k]

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dp = [[[] for _ in range(n+1)] for _ in range(10)]
        for i in range(10):
            dp[i][0].append([])
        for i in range(1, 10):
            for target in range(1, n+1):
                for item in dp[i-1][target]:
                    dp[i][target].append(item[:])
                if target >= i:
                    for item in dp[i-1][target-i]:
                        dp[i][target].append(item+[i])
        return [item for item in dp[9][n] if len(item) == k]

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dp = [[] for _ in range(n+1)]
        dp[0].append([])
        for i in range(1, 10):
            for target in range(n, i-1, -1):
                for item in dp[target-i]:
                    dp[target].append(item+[i])
        return [item for item in dp[n] if len(item) == k]

# @lc code=end
