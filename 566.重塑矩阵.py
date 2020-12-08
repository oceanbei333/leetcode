#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
from typing import List, Generator


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not len(nums) or len(nums)*len(nums[0]) != r*c:
            return nums
        alist = [[0]*c for _ in range(r)]
        for i, num_list in enumerate(nums):
            for j, val in enumerate(num_list):
                a_num = i*len(num_list) + j
                alist[a_num//c][a_num % c] = val
        return alist


# @lc code=end
