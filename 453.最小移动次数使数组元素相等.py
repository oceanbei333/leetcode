#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小移动次数使数组元素相等
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[index]-nums[0] for index in range(1,len(nums)) )
        
# @lc code=end

