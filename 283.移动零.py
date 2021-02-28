#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for item in nums[:]:
            if not item:
                nums.append(0)
                nums.remove(0)

    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for index, value in enumerate(nums[:]):
            if value:
                nums[pos], nums[index] = nums[index], nums[pos]
                pos += 1

# @lc code=end
