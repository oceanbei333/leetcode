#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
from collections import OrderedDict

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        for val in nums:
            if val in {first, second, third}:
                continue
            if val > first:
                third = second
                second = first
                first = val
            elif val > second:
                third = second
                second = val
            elif val > third:
                third = val
        print(first, second, third)
        if third == float('-inf'):
            return first
        else:
            return third

# @lc code=end
