#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def dp(index: int, used: List[int], target: int):
            for i in range(index, n):
                if target == candidates[i]:
                    res.append(used+candidates[i:i+1])
                elif target > candidates[i]:
                    dp(i, used+candidates[i:i+1], target-candidates[i])
        dp(0, [], target)
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        def dp(i:int,target: int):
            if not target:
                return [[]]
            if i < 1 or target < 0:
                return []
            res = dp(i-1, target)
            for alist in dp(i, target-candidates[i-1]):
                res.append(alist+[candidates[i-1]])
            return res
        return dp(n, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        dp = [[[] for _ in range(target+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0].append([])
        for i in range(1, n+1):
            for num in range(1, target+1):
                for item in dp[i-1][num]:
                    dp[i][num].append(item[:])
                if num >= candidates[i-1]:
                    for item in dp[i][num-candidates[i-1]]:
                        dp[i][num].append(item+[candidates[i-1]])
        return dp[n][target]

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        dp = [[] for _ in range(target+1)]
        dp[0].append([])
        for i in range(1, n+1):
            for num in range(candidates[i-1], target+1):
                for item in dp[num-candidates[i-1]]:
                    dp[num].append(item+[candidates[i-1]])
        return dp[target]









# @lc code=end
