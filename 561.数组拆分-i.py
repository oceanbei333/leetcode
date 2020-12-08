#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#

# @lc code=start
from typing import AsyncIterable, List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[index*2] for index in range(len(nums)//2))


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        alist = [0] * 20001
        lim = 10000
        for val in nums:
            alist[val+lim] += 1
        is_odd = False
        total = 0
        for val in range(-10000, 10001):
            #奇数的数量需要+1
            total += (alist[val+lim] + 1 - is_odd)//2 * val
            is_odd = not is_odd if alist[val+lim] % 2 else is_odd
        return total


# @lc code=end
