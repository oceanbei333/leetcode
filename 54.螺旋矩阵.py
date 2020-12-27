#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        total = rows*cols
        res = [None]*total
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direction_index = 0
        row, col = 0, 0
        for i in range(total):
            res[i] = matrix[row][col]
            matrix[row][col] = None
            next_row = row + directions[direction_index][0]
            new_col = col + directions[direction_index][1]
            if not (0 <= next_row < rows and 0 <= new_col < cols and matrix[next_row][new_col] is not None):
                direction_index = (direction_index+1) % 4
            row += directions[direction_index][0]
            col += directions[direction_index][1]
        return res

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res

        rows, columns = len(matrix), len(matrix[0])
        left, top, right, bottom = 0, 0, columns-1, rows-1
        while left <= right and top <= bottom:
            for column in range(left, right+1):
                res.append(matrix[top][column])

            for row in range(top+1, bottom+1):
                res.append(matrix[row][right])

            if left < right and top < bottom:
                for column in range(right-1, left, -1):
                    res.append(matrix[bottom][column])

                for row in range(bottom, top, -1):
                    res.append(matrix[row][left])
            left, top, right, bottom = left+1, top+1, right-1, bottom-1
        return res


# @lc code=end
