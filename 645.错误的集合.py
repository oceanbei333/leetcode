#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        aset = set(nums)
        bset = set(range(1, len(nums)+1))
        num =(bset - aset).pop()
        for val in nums:
            if val in aset:
                aset.remove(val)
            else:
                return [val, num]

    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        num_m = 1
        num_e = None
        for index in range(len(nums)-1):
            if nums[index] == nums[index+1]:
                num_e = nums[index]
            elif nums[index+1] - nums[index] != 1:
                num_m = nums[index]+1
        if nums[-1] != len(nums):
            num_m = len(nums)
        return [num_e,num_m]

        
# @lc code=end

