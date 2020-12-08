#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) -1
        result = []
        while i <= j:
            if A[i] + A[j] > 0:
                result.append(A[j]**2)
                j -= 1
            else:
                result.append(A[i]**2)
                i += 1
        return result[::-1]

class Solution(object):
    def sortedSquares(self, A):
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans

        
# @lc code=end

