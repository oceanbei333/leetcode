#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        i = 0
        for num in nums:
            if not counter[num]:
                continue
            if counter[num] > 1:
                counter[num] = 1
            else:
                counter[num] = 0
            nums[i] = num
            i += 1
        return i

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if nums[:i].count(num) < 2:
                nums[i] = num
                i += 1
        return i

    def removeDuplicates(self, nums: List[int]) -> int:
        i, count = 1, 1
        for index in range(1, len(nums)):
            if nums[index] != nums[index-1]:
                count = 0
            if count < 2:
                nums[i] = nums[index]
                count += 1
                i += 1
        return i

    def removeDuplicates(self, nums: List[int]) -> int:
        index, count = 1, 1
        while index < len(nums):
            if nums[index] == nums[index-1]:
                count += 1
                if count > 2:
                    nums.pop(index)
                    index -= 1
            else:
                count = 1
            index += 1
        return len(nums)


# @lc code=end
