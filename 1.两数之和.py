#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        alist = []
        for i in range(length):
            another_num = target - nums[i]
            if another_num not in alist:
                alist.append(nums[i])
            else:
                for index, num in enumerate(alist):
                    if num == another_num:
                        return [index, i]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        adict = dict()
        for index, value in enumerate(nums):
            another_num = target - value
            if another_num not in adict:
                adict[value] = index
            else:
                return [adict[another_num], index]

# @lc code=end
