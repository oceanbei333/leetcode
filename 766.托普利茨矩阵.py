#
# @lc app=leetcode.cn id=766 lang=python3
#
# [766] 托普利茨矩阵
#

# @lc code=start
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        length1 = len(matrix)
        length2 = len(matrix[0])
        for index in range(length1):
            val = matrix[index][0]
            i = index+1
            j = 1
            while i < length1 and j < length2:
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1
        for index in range(1, length2):
            val = matrix[0][index]
            i = 1
            j = index + 1

            while i < length1 and j < length2:
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1
        return True


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(not r or not c or val == matrix[r-1][c-1]
                   for r, row in enumerate(matrix) for c, val in enumerate)


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        adict = dict()
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in adict:
                    adict[r-c] = val
                else:
                    if adict[r-c] != val:
                        return False
        return True
# @lc code=end
