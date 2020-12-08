#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#

# @lc code=start

from collections import defaultdict
from functools import reduce

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_degee  = defaultdict(int)
        out_degee  = defaultdict(int)
        for out_v, in_v in trust:
            in_degee[in_v] += 1
            out_degee[out_v] += 1
        for i in range(1, N+1):
            if in_degee[i] == N-1 and not out_degee[i]:
                return i
        return -1
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_degee  = defaultdict(int)
        out_degee  = defaultdict(int)
        for out_v, in_v in trust:
            in_degee[in_v] += 1
            out_degee[out_v] += 1
        for i in range(1, N+1):
            if in_degee[i] == N-1 and not out_degee[i]:
                return i
        return -1
# @lc code=end

