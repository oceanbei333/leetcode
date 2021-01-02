#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber(self, nums: List[int]) -> int:
        aset = set()
        for val in nums:
            if val not in aset:
                aset.add(val)
            else:
                aset.remove(val)
        return aset.pop()

    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(None)
        for index in range(0, len(nums), 2):
            if nums[index] != nums[index+1]:
                return nums[index]


# @lc code=end
