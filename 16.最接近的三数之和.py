#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 10**4
        n = len(nums)
        for first in range(n-2):
            if first and nums[first] == nums[first-1]:
                continue
            second, third = first+1, n-1
            while second < third:
                sum_ = nums[first] + nums[second] + nums[third]
                if sum_ == target:
                    return sum_
                if abs(sum_-target) < abs(res - target):
                    res = sum_
                if sum_ < target:
                    while second < third and nums[second] == nums[second+1]:
                        second += 1
                    second += 1
                elif sum_ > target:
                    while second < third and nums[third] == nums[third-1]:
                        third -= 1
                    third -= 1
        return res
# @lc code=end
