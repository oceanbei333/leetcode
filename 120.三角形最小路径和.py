#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(None)
        def helper(row: int, index: int):
            if row >= len(triangle) or index >= len(triangle[row]):
                return 0
            return triangle[row][index] + min(helper(row+1, index), helper(row+1, index+1))
        return helper(0, 0)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle)-1, 0, -1):
            for index in range(len(triangle[row])-1):
                triangle[row-1][index] += min(triangle[row]
                                              [index], triangle[row][index+1])
        return triangle[0][0]


# @lc code=end
