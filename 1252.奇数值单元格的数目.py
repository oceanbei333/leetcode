#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
#

# @lc code=start
from typing import List
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        A_n = [0]* n
        A_m = [0]* m
        for i, j in indices:
            A_n[i] += 1
            A_m[j] += 1
        
        return sum((i+j)%2 for i in A_n for j in A_m)
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        A_n = [False]* n
        A_m = [False]* m
        for i, j in indices:
            A_n[i] ^= 1
            A_m[j] ^= 1
        a_true_n = sum(A_n)
        a_true_m = sum(A_m)
        return a_true_n * (m- a_true_m) + (n-a_true_n) * a_true_m
        
# @lc code=end

