#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r_len = len(grid)
        c_len = len(grid[0])
        def dfs(r:int, c:int)->int:
            if r<0 or c<0 or r >= r_len or c >= c_len:
                return 1 
            if not grid[r][c]:
                return 1
            if grid[r][c] != 1:
                return 0
            grid[r][c] = 2
            return (
                dfs(r,c+1)+dfs(r, c-1)+dfs(r-1, c)+dfs(r+1, c)
            )
        for i in range(r_len):
            for j in range(c_len):
                if grid[i][j] == 1:
                    return dfs(i, j)
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res += 4
                    if j>=1 and grid[i][j-1]:
                        res -= 2
                    if i>=1 and grid[i-1][j]:
                        res -= 2
        return res


                

# @lc code=end

