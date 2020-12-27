#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] == target:
                return mid
            # 只能在有序序列中进行二分查找
            # nums[:mid+1] 升序
            if nums[left] <= nums[mid]:
                # target 在 nums[:mid+1]
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    # target 在 nums[mid+1:]
                    left = mid+1
            else:
                # nums[mid:] 升序
                if nums[mid] < target <= nums[right]:
                    # target 在 nums[mid+1:]
                    left = mid+1
                else:
                    # target 在 nums[:mid]
                    right = mid - 1
        return -1
# @lc code=end
