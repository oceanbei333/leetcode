#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
from typing import List
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
        nums[1] = max(nums[:2])
        for i in range(2, length):
            nums[i] = max(nums[i]+nums[i-2], nums[i-1])
        return max(nums)
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        for i in range(1, len(nums)-1):
            nums[i] = max(nums[i]+nums[i-2], nums[i-1])
        return max(nums)
    def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre+num, cur), cur
        return cur
            

# @lc code=end

