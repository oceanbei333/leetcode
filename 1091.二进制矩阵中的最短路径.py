#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
from typing import List, Set, Tuple


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols, count = len(grid), len(grid[0]), 0
        if grid[0][0] or grid[-1][-1]:
            return -1
        points = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
        queue = [(0, 0)]
        while queue:
            count += 1
            new_queue = []
            for x, y in queue:
                if x == rows-1 and y == cols-1:
                    return count
                for i, j in points:
                    r, c = x+i, y+j
                    if 0 <= r < rows and 0 <= c < cols and not grid[r][c]:
                        grid[r][c] = 1
                        new_queue.append((r, c))
            queue = new_queue
        return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols, count = len(grid), len(grid[0]), 0
        if grid[0][0] or grid[-1][-1]:
            return -1
        if cols == 1:
            return 1
        points = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
        front = {(0, 0)}
        visited = set()
        back = {(rows-1, cols-1)}
        while front:
            count += 1
            new_queue = set()
            visited |= front
            for x, y in front:
                for i, j in points:
                    r, c = x+i, y+j
                    if (r, c) in back:
                        return count + 1
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and not grid[r][c]:
                        new_queue.add((r, c))
            front = new_queue
            if len(front) > len(back):
                front, back = back, front
        return -1

# @lc code=end
