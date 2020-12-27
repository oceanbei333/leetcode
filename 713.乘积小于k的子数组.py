#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#

# @lc code=start
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        start, end = 0, 0
        n = len(nums)
        res = 0
        total = 1
        while end < n:
            total *= nums[end]
            while start < n and total >= k:
                total /= nums[start]
                start += 1
            res += end - start + 1
            end += 1
        return res

# @lc code=end
