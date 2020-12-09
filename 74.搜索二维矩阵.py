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
        n = len(matrix) 
        if not n:
            return False
        m = len(matrix[0])
        if not m:
            return False
        l,r = 0, n -1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid -1
            else:
                l = mid+1
        col = l -1
        l, r = 0, m-1
        while l<=r:
            mid = (l+r)//2
            if matrix[col][mid] == target:
                return True
            elif matrix[col][mid] > target:
                r = mid -1
            else:
                l = mid+1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        alist =  []
        for row in matrix:
            alist.extend(row)
        l, r = 0, len(alist) -1
        while l <= r:
            mid = (l+r)//2
            if alist[mid] == target:
                return True
            if alist[mid] > target:
                r = mid -1
            else:
                l= mid+1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        aset = reduce(lambda x, y: set(x)|set(y), matrix)
        return target in aset
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        alist = reduce(lambda x, y: x+y, matrix)
        l, r = 0, len(alist) -1
        while l <= r:
            mid = (l+r)//2
            if alist[mid] == target:
                return True
            if alist[mid] > target:
                r = mid -1
            else:
                l= mid+1
        return False

            
# @lc code=end


