#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i = len(grid[0])
        total = 0
        for r, row in enumerate(grid):
            for index in range(i):
                if row[index] <0:
                    total += ( len(grid) - r )*(i-index)
                    i = index
                    break
        return total


        
# @lc code=end

