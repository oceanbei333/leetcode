#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#

# @lc code=start
from collections import defaultdict
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        alist = [[]for _ in range(200)]
        for i in range(R):
            for j in range(C):
                alist[abs(i-r0)+abs(j-c0)].append([i,j])
        res = []
        for i in alist:
            if i:
                res.extend(i)
            else:
                break
        return res
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        adict = defaultdict(list)
        for i in range(R):
            for j in range(C):
                adict[abs(i-r0)+abs(j-c0)].append([i,j])
        res = []
        for i in range(200):
            if adict[i]:
                res.extend(adict[i])
        return res
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        for i in range(R):
            for j in range(C):
                res.append([i, j])
        return sorted(res, key=lambda x: abs(x[0]-r0)+abs(x[1]-c0))
# @lc code=end


