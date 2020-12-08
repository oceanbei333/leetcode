#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 重复 N 次的元素
#

# @lc code=start
from random import choice
from typing import Counter, List
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        while True:
            s = choice(A)
            if A.count(s) == len(A)//2:
                return s
    def repeatedNTimes(self, A: List[int]) -> int:
        A.sort()
        half = len(A)//2
        if A[0] == A[half-1]:
            return A[0]
        if A[-1] == A[half]:
            return A[-1]
        return A[half]
    def repeatedNTimes(self, A: List[int]) -> int:
        counter = Counter(A)
        for num, count in counter.items():
            if count == 1:
                return num
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(len(A)):
            for j in range(1, 4):
                if (i+j)<len(A) and A[i] == A[i+j]:
                    return A[i]
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(1, 4):
            for j in range(len(A)-i):
                if A[j] ==A[j+i]:
                    return A[j]

# @lc code=end

