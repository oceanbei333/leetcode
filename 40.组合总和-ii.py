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
                    res.append(used+candidates[j:j+1])
                elif target > candidates[j]:
                    dp(used+[candidates[j]], j+1, target-candidates[j])
        dp([], 0, target)
        return res

# @lc code=end
