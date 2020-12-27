#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        tmp = [row[:] for row in board]
        for r in range(rows):
            for c in range(cols):
                r_start = r-1 if r else 0
                c_start = c-1 if c else 0
                count = sum(sum(row[c_start:c+2])
                            for row in tmp[r_start:r+2]) - tmp[r][c]

                if tmp[r][c] and (count < 2 or count > 3):
                    board[r][c] = 0
                if not tmp[r][c] and count == 3:
                    board[r][c] = 1

    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        neighbors = ((1, 0), (1, -1), (0, -1), (-1, -1),
                     (-1, 0), (-1, 1), (0, 1), (1, 1))

        def get_count(r: int, c: int):
            count = 0
            for r_diff, c_diff in neighbors:
                next_r, next_c = r+r_diff, c+c_diff
                if 0 <= next_r < rows and 0 <= next_c < cols and board[next_r][next_c] != 2:
                    count += abs(board[next_r][next_c])
            return count

        for r in range(rows):
            for c in range(cols):
                count = get_count(r, c)
                if board[r][c] and (count < 2 or count > 3):
                    board[r][c] = -1
                elif not board[r][c] and count == 3:
                    board[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 0
                if board[r][c] == 2:
                    board[r][c] = 1


# @lc code=end
