#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        block = [[set() for _ in range(3)] for _ in range(3)]
        nums = set(str(num) for num in range(1, 10))
        for x in range(9):
            for y in range(9):
                block[x//3][y//3].add(board[x][y])
                row[x].add(board[x][y])
                col[y].add(board[x][y])

        def dfs(board, index: int):
            if index == 81:
                return True
            x = index//9
            y = index % 9
            if board[x][y] != '.':
                return dfs(board, index+1)
            for num in nums - (row[x] | col[y] | block[x//3][y//3]):
                row[x].add(num)
                col[y].add(num)
                block[x//3][y//3].add(num)
                board[x][y] = num
                if dfs(board, index+1):
                    return True
                board[x][y] = '.'
                row[x].remove(num)
                col[y].remove(num)
                block[x//3][y//3].remove(num)
            return False
        dfs(board, 0)

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nums = set(str(num) for num in range(1, 10))
        row = [nums.copy() for _ in range(9)]
        col = [nums.copy() for _ in range(9)]
        block = [[nums.copy() for _ in range(3)] for _ in range(3)]
        empty = []
        for x in range(9):
            for y in range(9):
                if board[x][y] == '.':
                    empty.append((x, y))
                else:
                    block[x//3][y//3].remove(board[x][y])
                    row[x].remove(board[x][y])
                    col[y].remove(board[x][y])

        def dfs(index: int):
            if index < 0:
                return True
            x, y = empty[index]
            if board[x][y] != '.':
                return dfs(index-1)
            for num in (row[x] & col[y] & block[x//3][y//3]):
                row[x].remove(num)
                col[y].remove(num)
                block[x//3][y//3].remove(num)
                board[x][y] = num
                if dfs(index-1):
                    return True
                board[x][y] = '.'
                row[x].add(num)
                col[y].add(num)
                block[x//3][y//3].add(num)
            return False
        dfs(len(empty)-1)

# @lc code=end
