#
# @lc app=leetcode.cn id=1464 lang=python3
#
# [1464] 数组中两元素的最大乘积
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_n = max(nums)
        nums.remove(max_n)
        sec_n = max(nums)
        return ( max_n -1) *(sec_n-1)
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)
# @lc code=end

