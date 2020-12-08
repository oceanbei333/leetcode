#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
from typing import List
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        length1 = len(A)
        length2 = len(A[0])
        A_t = [[0]*length1 for _ in range(length2)]
        for r in range(length2):
            for c in range(length1):
                A_t = A[c][r]
        retturn A_t

        
# @lc code=end

