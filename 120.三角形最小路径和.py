#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def _minimumTotal(row: int, index: int):
            if row >= len(triangle) or index >= len(triangle[row]):
                return 0
            return triangle[row][index] + min(_minimumTotal(row+1, index), _minimumTotal(row+1, index+1))
        return _minimumTotal(0, 0)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-1, 0, -1):
            for j in range(len(triangle[i])-1):
                triangle[i-1][j] += min(triangle[i][j], triangle[i][j+1])
        return triangle[0][0]


# @lc code=end
