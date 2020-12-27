#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
from typing import List
from functools import reduce


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        alist = [num for row in matrix for num in row]
        l, r = 0, len(alist) - 1
        while l <= r:
            mid = (l+r) >> 1
            if alist[mid] == target:
                return True
            if alist[mid] > target:
                r = mid - 1
            else:
                l = mid+1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, rows*cols-1
        while l <= r:
            mid = (l+r) >> 1
            row = mid // cols
            col = mid - (row*cols)
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid+1
        return False

# @lc code=end
