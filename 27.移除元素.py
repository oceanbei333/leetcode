#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        for index in range(len(nums)):
            if val != nums[index]:
                nums[pos] = nums[index]
                pos += 1
        return pos


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        length = len(nums)
        while index < length:
            if nums[index] == val:
                nums[index] = nums[length-1]
                length -= 1
            else:
                index += 1
        return index

# @lc code=end
