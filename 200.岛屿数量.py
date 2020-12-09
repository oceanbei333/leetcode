#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
from typing import List, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
                    queue = [(r, c)]
                    while queue:
                        r, c = queue.pop()
                        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
                            grid[r][c] = '0'
                            queue.extend(
                                [(r, c+1), (r, c-1), (r+1, c), (r-1, c)])
        return res

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r: int, c: int):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
                grid[r][c] = '0'
                for x, y in ((r, c+1), (r, c-1), (r+1, c), (r-1, c)):
                    dfs(x, y)
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
        return res

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dsu = list(range(rows*cols))

        def find(x: int) -> int:
            if dsu[x] != x:
                dsu[x] = find(dsu[x])
            return dsu[x]

        def union(x1: int, x2: int):
            dsu[find(x2)] = find(x1)

        for r in range(rows):
            for c in range(cols):
                x1 = r*cols+c
                if grid[r][c] == "1":
                    for x, y in [(r + 1, c), (r, c + 1)]:
                        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
                            union(x1, x*cols+y)
        aset = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    aset.add(find(r*cols+c))
        return len(aset)


# @lc code=end
