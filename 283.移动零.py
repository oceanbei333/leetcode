#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                if i != pos:
                    nums[pos] = nums[i]
                    nums[i] = 0
                    pos += 1
                    break
                pos += 1

        for j in range(i+1, len(nums)):
            if nums[j]:
                nums[pos] = nums[j]
                nums[j] = 0
                pos += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for item in nums[:]:
            if not item:
                nums.append(0)
                nums.remove(0)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for index, value in enumerate(nums[:]):
            if value:
                if index != pos:
                    nums[pos], nums[index] = nums[index], nums[pos]
                pos += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for index in range(len(nums)):
            if nums[index]:
                if index != pos:
                    nums[pos], nums[index] = nums[index], nums[pos]
                pos += 1


# @lc code=end
