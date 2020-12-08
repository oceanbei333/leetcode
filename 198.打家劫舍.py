#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        alist = [nums[0], max(*nums[:2])]
        for index in  range(2, length):
            alist.append(max(alist[index-1], alist[index-2]+ nums[index] ))
        return max(alist)
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        nums[1] = max(*nums[:2])
        for index in range(2, length):
            nums[index] = max(nums[index]+nums[index-2], nums[index-1])
        return max(nums)
        

        
# @lc code=end

