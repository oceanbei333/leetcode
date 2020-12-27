#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(alist: List[int]):
            index = bisect.bisect_left(alist, target)
            if index < len(alist) and alist[index] == target:
                return True
            return False
        return any(search(row) for row in matrix)

    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(l, u, r, d):
            # this submatrix has no height or no width.
            if l > r or u > d:
                return False
            mid = (u+d) >> 1
            # 找到第一个比target大的元素
            col = bisect.bisect_left(matrix[mid], target)
            if col <= r and matrix[mid][col] == target:
                return True
            return search_rec(l, mid+1, col-1, d) or search_rec(col, u, r, mid-1)
        return search_rec(0, 0, len(matrix[0])-1, len(matrix)-1)

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        r, c = rows-1, 0
        while r >=0 and c < cols:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                c +=1
            elif matrix[r][c] > target:
                r -= 1
        return False
            


# @lc code=end
