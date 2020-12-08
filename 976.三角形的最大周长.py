#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#

# @lc code=start
from typing import List
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for index in range(len(A)-2):
            if A[index] < A[index+1] +A[index+2]:
                return A[index] + A[index+1] +A[index+2]
        return 0
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for index in range(len(A)-1, 1, -1):
            if A[index] < A[index-1] +A[index-2]:
                return A[index] + A[index-1] +A[index-2]
        return 0
        
# @lc code=end

