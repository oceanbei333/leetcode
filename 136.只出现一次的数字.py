#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        nums.append(float('inf'))
        for index in range(0,length,2):
            if nums[index] != nums[index+1]:
                return nums[index]
    def singleNumber(self, nums: List[int]) -> int:
        adict = dict()
        for val in nums:
            if val not in adict:
                adict[val] = None
            else:
                adict.pop(val)
        return adict.popitem()[0]
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(lambda x,y: x^y nums)
# @lc code=end

