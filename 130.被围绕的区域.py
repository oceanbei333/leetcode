#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        dsu = list(range(rows*cols))

        def find(x: int):
            if dsu[x] != x:
                dsu[x] = find(dsu[x])
            return dsu[x]

        def union(x: int, y: int):
            dsu[find(x)] = find(y)

        for x in range(rows-1):
            for y in range(cols-1):
                if board[x][y] == 'O':
                    for r, c in ((x+1, y), (x, y+1)):
                        if r < rows and c < cols and board[r][c] == 'O':
                            union(x*cols+y, r*cols+c)
        edge_x = set()
        for x in range(1, rows-1):
            edge_x.add(find(x*cols))
            edge_x.add(find(x*cols+cols-1))
        for y in range(1, cols-1):
            edge_x.add(find(y))
            edge_x.add(find(cols*(rows-1)+y))
        for x in range(1, rows-1):
            for y in range(1, cols-1):
                if board[x][y] == 'O' and find(x*cols+y) not in edge_x:
                    board[x][y] = 'X'

    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        rows = len(board)
        cols = len(board[0])

        def dfs(x: int, y: int):
            if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'O':
                board[x][y] = 'A'
                for r, c in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    dfs(r, c)
        for x in range(rows):
            dfs(x, 0)
            dfs(x, cols-1)
        for y in range(cols):
            dfs(0, y)
            dfs(rows-1, y)
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == 'A':
                    board[x][y] = 'O'
                elif board[x][y] == 'O':
                    board[x][y] = 'X'

    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        rows = len(board)
        cols = len(board[0])

        def bfs(x: int, y: int):
            queue = [(x, y)]
            while queue:
                new_queue = []
                for x, y in queue:
                    if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'O':
                        board[x][y] = 'A'
                        new_queue.extend(
                            [(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
                queue = new_queue

        for x in range(rows):
            bfs(x, 0)
            bfs(x, cols-1)
        for y in range(cols):
            bfs(0, y)
            bfs(rows-1, y)
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == 'A':
                    board[x][y] = 'O'
                elif board[x][y] == 'O':
                    board[x][y] = 'X'


# @lc code=end
