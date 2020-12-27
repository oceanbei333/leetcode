#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums

    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] == target:
                return True
            if nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid + 1
            elif nums[mid] < nums[l]:
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid - 1
            else:
                l += 1
        return False

# @lc code=end
