#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix))]
        area = 0
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                w = dp[x][y] = dp[x][y-1] + 1 if matrix[x][y] == '1' else 0
                for i in range(x, -1, -1):
                    w = min(w, dp[i][y])
                    h = (x-i+1)
                    area = max(area, w*h)
        return area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        cols = len(matrix[0])
        dp = [0]*(cols+1)
        area = 0
        for x in range(len(matrix)):
            for y in range(cols):
                dp[y] = dp[y] + 1 if matrix[x][y] == '1' else 0
            stack = [-1]
            for i in range(cols+1):
                while dp[stack[-1]] > dp[i]:
                    area = max(area, dp[stack.pop()]*(i-stack[-1]-1))
                stack.append(i)
        return area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        cols = len(matrix[0])
        height = [0]*cols
        # left is the left ,but right is next one ,so right-left=width
        left = [0]*cols
        right = [cols]*cols
        area = 0
        for x in range(len(matrix)):
            cur_left, cur_right = 0, cols
            for y in range(cols):
                if matrix[x][y] == '1':
                    height[y] += 1
                    left[y] = max(left[y], cur_left)
                else:
                    height[y] = 0
                    left[y] = 0
                    cur_left = y + 1

                y = cols - 1 - y
                if matrix[x][y] == '1':
                    right[y] = min(right[y], cur_right)
                else:
                    right[y] = cols
                    cur_right = y
            area = max(area, max(height[y]*(right[y]-left[y])
                                 for y in range(cols)))
        return area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        height = [[0]*(cols+1) for i in range(rows)]
        left = [[0]*(cols+1) for i in range(rows)]
        right = [[cols]*(cols+1) for i in range(rows)]
        area = 0
        for x in range(rows):
            cur_left, cur_right = 0, cols
            for y in range(cols):
                if matrix[x][y] == '1':
                    height[x][y] = height[x-1][y] + 1
                    left[x][y] = max(left[x-1][y], cur_left)
                else:
                    cur_left = y+1
                y = cols-1-y
                if matrix[x][y] == '1':
                    right[x][y] = min(right[x-1][y], cur_right)
                else:
                    cur_right = y
                area = max(
                    area, max(height[x][y]*(right[x][y]-left[x][y]) for y in range(cols)))
        return area

# @lc code=end
