#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        @lru_cache(len(nums)-1)
        def dp(day: int) -> int:
            if not day:
                return nums[day]
            if day == 1:
                return max(nums[:2])
            return max(nums[day]+dp(day-2), dp(day-1))
        return dp(len(nums)-1)

    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        for i in range(1, len(nums)-1):
            nums[i] = max(nums[i]+nums[i-2], nums[i-1])
        return max(nums)

    def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre+num, cur), cur
        return cur

# @lc code=end
