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
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[right]<nums[left]:
                if nums[right] == target:
                    return right
                else:
                    right -= 1
                if nums[left] == target:
                    return left
                else:
                    left += 1
            else:
                if nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[mid] > target>=nums[0]:
                    right  = mid -1
                else:
                    left = mid+1
            else:
                if nums[mid] < target<=nums[-1]:
                    left = mid+1
                else:
                    right = mid -1
        return -1
# @lc code=end

