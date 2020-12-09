#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(nums: List[int]) -> int:
            nums.append(0)
            for i in range(1, len(nums)-1):
                nums[i] = max(nums[i]+nums[i-2], nums[i-1])
            return max(nums)
        return max(_rob(nums[1:]), _rob(nums[:-1]), nums[0])

    def rob(self, nums: List[int]) -> int:
        def _rob(nums: List[int]) -> int:
            cur, pre = 0, 0
            for val in nums:
                cur, pre = max(pre+val, cur), cur
            return cur
        return max(_rob(nums[1:]), _rob(nums[:-1]), nums[0])
# @lc code=end
