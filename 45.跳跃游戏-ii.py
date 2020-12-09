#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        nums[-1] = 0
        for i in range(l-2, -1, -1):
            max_index = i+nums[i]
            nums[i] = float('inf')
            nums[i] = min(nums[i:max_index+1])+1
        return nums[0]

    def jump(self, nums: List[int]) -> int:
        cur_max, pre_max, step = 0, 0, 0
        l = len(nums)
        for i in range(l-1):
            cur_max = max(cur_max, i+nums[i])
            if i == pre_max:
                step += 1
                pre_max = cur_max
        return step

    def jump(self, nums: List[int]) -> int:
        cur_max, pre_max, step = 0, 0, 0
        l = len(nums)
        for i in range(l-1):
            cur_max = max(cur_max, i+nums[i])
            if cur_max >= l - 1:
                return step + 1
            if i == pre_max:
                step += 1
                pre_max = cur_max
        return 0

# @lc code=end
