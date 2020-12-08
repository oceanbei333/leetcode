#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
from typing import List
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        for index in range(len(A)):
            if not index:
                pre = A[index]
            if index < len(A) -1 :
                if pre < A[index] > A[index+1] or pre > A[index] < A[index+1]:
                    return False
                if A[index] !=A[index+1]:
                    pre = A[index]
        return True

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        pre = A[0]
        for index in range(1, len(A)-1):
            if pre < A[index] > A[index+1] or pre > A[index] < A[index+1]:
                return False
            if A[index] !=A[index+1]:
                pre = A[index]
        return True



        
# @lc code=end

