#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        for num, count in Counter(nums).items():
            if count == 1:
                return num

    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num

    def singleNumber(self, nums: List[int]) -> int:
        adict = dict()
        for num in nums:
            if num not in adict:
                adict[num] = True
            else:
                adict[num] = False
        for num in adict:
            if adict[num]:
                return num
# @lc code=end
