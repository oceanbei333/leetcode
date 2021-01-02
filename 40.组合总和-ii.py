#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def dp(used: List[int], index, target: int):
            for j in range(index, n):
                if j > index and candidates[j] == candidates[j-1]:
                    continue
                if target == candidates[j]:
                    res.append(used+[candidates[j]])
                elif target > candidates[j]:
                    dp(used+[candidates[j]], j+1, target-candidates[j])
        dp([], 0, target)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()

        def dp(count: int, target: int):
            if not target:
                return[[]]
            if count < 1 or target < 0:
                return []
            index = count
            while index > 1 and candidates[index-1] == candidates[index-2]:
                index -= 1
            res = dp(index-1, target)
            for item in dp(count-1, target-candidates[count-1]):
                res.append(item+[candidates[count-1]])
            return res
        return dp(n, target)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        dp = [[[] for _ in range(target+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0].append([])
        for i in range(1, n+1):
            for num in range(1, target+1):
                index = i
                while index > 1 and candidates[index-1] == candidates[index-2]:
                    index -= 1
                for item in dp[index-1][num]:
                    dp[i][num].append(item[:])
                if num >= candidates[i-1]:
                    for item in dp[i-1][num-candidates[i-1]]:
                        dp[i][num].append(item+[candidates[i-1]])
        return dp[n][target]

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        dp = [[] for _ in range(target+1)]
        dp[0].append([])
        for i in range(1, n+1):
            for num in range(target, candidates[i-1]-1, -1):
                for item in dp[num-candidates[i-1]]:
                    if item + [candidates[i-1]] not in dp[num]:
                        dp[num].append(item+[candidates[i-1]])
        return dp[target]
# @lc code=end
