#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#

# @lc code=start
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(num for row in matrix for num in row)[k-1]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        from heapq import heappush, heappop
        heap = []
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            heappush(heap, (matrix[row][0], row, 0))
        res = None
        while k:
            k -= 1
            res, row, col = heappop(heap)
            col += 1
            if col < cols:
                heappush(heap, (matrix[row][col], row, col))
        return res

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        def check(mid):
            row, col, num = rows - 1, 0, 0
            while row >= 0 and col < cols:
                if matrix[row][col] <= mid:
                    num += row + 1
                    col += 1
                else:
                    row -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return right

# @lc code=end
