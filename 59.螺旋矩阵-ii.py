#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        i = 1
        while left <=right and top <=right:
            for col in range(left, right+1):
                matrix[top][col] =i
                i+= 1
            for row in range(top+1, bottom+1):
                matrix[row][right] = i
                i += 1
            for  col in range(right-1, left, -1):
                matrix[bottom][col] = i
                i += 1
            for row in range(bottom, top, -1):
                matrix[row][left] = i
                i += 1

            left, right, top, bottom = left+1, right-1, top+1, bottom -1
        return matrix
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None]*n for _ in range(n)]
        total = n*n
        row, col = 0, 0
        directions = ((0, 1), (1, 0),(0, -1),(-1, 0))
        direction_index = 0
        for i in range(1,total+1):
            matrix[row][col] = i
            new_row = row + directions[direction_index][0]
            new_col = col + directions[direction_index][1]
            if not (0<=new_row<n and 0<=new_col<n and matrix[new_row][new_col] is None):
                direction_index = (direction_index+1)%4
            row += directions[direction_index][0]
            col += directions[direction_index][1]
        return matrix



# @lc code=end

