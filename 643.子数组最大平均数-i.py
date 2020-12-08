#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_num = pre = sum(nums[:k])
        for index in range(1, 1+len(nums)-k):
            cur = pre-nums[index-1] + nums[index+k-1]
            max_num = max(max_num, cur)
            pre = cur
        return max_num/k

        # @lc code=end
