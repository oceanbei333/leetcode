#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        @lru_cache(target)
        def dp(target: int):
            if target < 0:
                return []
            if not target:
                return [[]]
            res = []
            for candidate in candidates:
                for alist in dp(target-candidate):
                    new_list = sorted(alist+[candidate])
                    if new_list not in res:
                        res.append(new_list)
            return res
        return dp(target)

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
        from collections import defaultdict
        dp = defaultdict(list)
        dp[0].append([])
        for cand in candidates:
            for num in range(cand, target+1):
                dp[num].extend([alist+[cand] for alist in dp[num-cand]])
        return dp[target]


# @lc code=end
