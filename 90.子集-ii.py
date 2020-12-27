#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(i, used):
            if i == len(nums):
                res.append(used[:])
            else:
                if not used or nums[i] != used[-1]:
                    helper(i+1, used)
                used.append(nums[i])
                helper(i+1, used)
                used.pop()
        nums.sort()
        helper(0, [])
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(i, used):
            if i < 0:
                res.append(used)
            else:
                if not used or nums[i] != used[-1]:
                    helper(i-1, used)
                helper(i-1, used+[nums[i]])
        nums.sort()
        helper(len(nums)-1, [])
        return res

# @lc code=end
