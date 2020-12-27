#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        row_flag = [False]*rows
        col_flag = [False]*cols
        for row in range(rows):
            for col in range(cols):
                if not matrix[row][col]:
                    row_flag[row] = True
                    col_flag[col] = True
        for row in range(rows):
            for col in range(cols):
                if row_flag[row] or col_flag[col]:
                    matrix[row][col] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        for row in range(rows):
            for col in range(cols):
                if not matrix[row][col]:
                    if not row:
                        first_row_zero = True
                    if not col:
                        first_col_zero = True
                    if row and col:
                        matrix[0][col] = 0
                        matrix[row][0] = 0
        for row in range(1, rows):
            for col in range(1, cols):
                if not matrix[0][col] or not matrix[row][0]:
                    matrix[row][col] = 0
        
        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0
        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0



# @lc code=end
