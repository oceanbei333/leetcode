#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#

# @lc code=start
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        list_left = nums[:]
        list_right = nums[:]
        for index in list(range(len(list_right)-2, - 1, -1)):
            list_right[index] += list_right[index+1]
        for index in range(len(list_left)):
            if index:
                list_left[index] += list_left[index-1]
            if list_left[index] == list_right[index]:
                return index
        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for index in list(range(len(nums)-2, - 1, -1)):
            nums[index] += nums[index+1]
        for index in range(len(nums)):
            total_left = nums[index]
            if not index:
                nums[index] -= nums[index+1]
            elif index < len(nums)-1:
                nums[index] = nums[index] - nums[index+1] + nums[index-1]
            else:
                nums[index] = nums[index] + nums[index-1]
            if total_left == nums[index]:
                return index
        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        left_sum = 0
        for index in range(len(nums)):
            if left_sum == S-left_sum-nums[index]:
                return index
            left_sum += nums[index]
        return -1


# @lc code=end
