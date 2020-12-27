#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# @lc code=start
from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        len_a = len(A)
        len_b = len(B)
        dp = [[0]*(len_a+1) for _ in range(len_b+1)]
        for i in range(len_a):
            for j in range(len_b):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1]+1
        return max(max(item) for item in dp)

    def findLength(self, A: List[int], B: List[int]) -> int:
        la, lb = len(A), len(B)

        def maxL(indexA: int, indexB: int) -> int:
            length = cur = 0
            while indexA < la and indexB < lb:
                if A[indexA] == B[indexB]:
                    cur += 1
                    length = max(length, cur)
                else:
                    cur = 0
                indexA += 1
                indexB += 1
            return length

        ret1 = max(maxL(i, 0) for i in range(la))
        ret2 = max(maxL(0, i) for i in range(lb))
        return max(ret1, ret2)
# @lc code=end
