#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        dp = [[0]*(len(matrix[0])) for _ in range(len(matrix))]
        area = 0
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == '1':
                    w = dp[x][y] = dp[x][y-1] + 1
                    for i in range(x, -1, -1):
                        w = min(w, dp[i][y])
                        h = x - i + 1
                        area = max(area, h*w)
        return area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        area = 0
        cols = len(matrix[0])
        heights = [0]*(cols+1)
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                heights[y] = heights[y] +1 if matrix[x][y] == '1' else 0
            # 84 题
            stack = [-1]
            for i in range(cols+1):
                while heights[stack[-1]] > heights[i]:
                    area = max(area, heights[stack.pop()]*(i-stack[-1]-1))
                stack.append(i)
        return area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        height = [0]*cols
        left = [0]*cols
        right = [0]*cols
        area = 0
        for x in range(rows):
            for y in range(cols):
                if matrix[x][y] == '1':
                    height[y] += 1
                else:
                    height[y] = 1
            cur_left, cur_right = 0, cols
            for y in range(cols):
                if matrix[x][y] == '1':
                    left[y] = max(left[y], cur_left)
                else:
                    left[y] = 0
                    cur_left = y+1
            for y in range(cols):
                if matrix[x][y] == '1':
                    right[y] = min(right[y], cur_right)
                else:
                    right[y] = 0
                    cur_right = y-1
            area = max(area, max(height[y]*(right[y]-left[y]) for y in range(cols)))
        return area

            


# @lc code=end
