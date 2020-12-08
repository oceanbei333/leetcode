#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        if all(m >= 2*val for val in nums if val != m):
            return nums.index(m)
        return -1
# @lc code=end
