#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import Counter
        countAB = Counter([a+b for a in A for b in  B])
        return sum(countAB[-c-d] for c in C for d in D )
# @lc code=end
