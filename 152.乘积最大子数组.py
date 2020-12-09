#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = min_ = max_ = nums[0]
        for val in nums[1:]:
            vals = (val, val*min_, val*max_)
            min_, max_ = min(vals),max(vals)
            ans = max(ans, max_)
        return ans
# @lc code=end

