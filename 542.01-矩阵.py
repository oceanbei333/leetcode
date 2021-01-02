#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        dist = [[0] * cols for _ in range(rows)]
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        queue = {(r, c) for r in range(rows)
                 for c in range(cols) if not matrix[r][c]}
        # 将所有的 0 添加进初始队列中
        visited = set()

        # 广度优先搜索
        while queue:
            new_queue = set()
            visited |= queue
            for r, c in queue:
                for r_diff, c_diff in directions:
                    nr, nc = r+r_diff, c+c_diff
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        dist[nr][nc] = dist[r][c] + 1
                        new_queue.add((nr, nc))
            queue = new_queue
        return dist

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dp = [[float('inf')] * (cols+1) for _ in range(rows+1)]
        # 如果 (r, c) 的元素为 0，那么距离为 0
        for r in range(rows):
            for c in range(cols):
                if not matrix[r][c]:
                    dp[r][c] = 0

        def get_val(r, c):
            dp[r][c] = min(
                dp[r][c],
                dp[r - 1][c] + 1, dp[r][c - 1] + 1,
                dp[r + 1][c] + 1, dp[r][c + 1] + 1
            )
        for r in range(rows):
            for c in range(cols):
                get_val(r, c)
        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                get_val(r, c)
        res = [row[:cols] for row in dp[:rows]]
        return res

# @lc code=end
