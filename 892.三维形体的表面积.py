#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        res = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    res += 2
                    for x,y in (i, j+1), (i, j-1), (i-1,j), (i+1, j):
                        if 0<=x<N and 0<=y<N:
                            h = grid[x][y]
                        else:
                            h = 0
                        res += max(grid[i][j]-h, 0)
        return res



# @lc code=end



