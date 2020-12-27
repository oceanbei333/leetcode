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
            if index < 0 or target<0 or len(used) > k:
                return
            helper(index-1, used, target)
            helper(index-1, used+[nums[index]], target-nums[index])
        helper(8, [], n)
        return res


# @lc code=end
