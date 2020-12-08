#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        adict = dict()
        for index, num in enumerate(sorted((nums))):
            if num not in adict:
                adict[num] = index
        for index in range(len(nums)):
            nums[index] = adict[nums[index]]
        return nums

# @lc code=end

