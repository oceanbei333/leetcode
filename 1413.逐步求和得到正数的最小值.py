#
# @lc app=leetcode.cn id=1413 lang=python3
#
# [1413] 逐步求和得到正数的最小值
#

# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for index in range(1, len(nums)):
            nums[index] += nums[index-1]
        min_n = min(nums)
        return 1 if min_n > 0 else 1-min_n
            
# @lc code=end

