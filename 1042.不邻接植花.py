#
# @lc app=leetcode.cn id=1042 lang=python3
#
# [1042] 不邻接植花
#

# @lc code=start
from collections import defaultdict
from typing import List
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        if not paths:
            return [1]*n
        adict = defaultdict(list)
        res = [0]*n
        for src , dest in paths:
            adict[src-1].append(dest-1)
            adict[dest-1].append(src-1)
        for index in range(n):
            res[index] = ({1,2,3,4} - {res[i] for i in adict[index]}).pop()
        return res


# @lc code=end

