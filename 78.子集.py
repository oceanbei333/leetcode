#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res.extend([sub+[num] for sub in res])
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def _subsets(i: int, used: List[int]):
            if i < 0:
                return [used]
            return _subsets(i-1, used) + _subsets(i-1, used+[nums[i]])

        return _subsets(len(nums)-1, [])
# @lc code=end
