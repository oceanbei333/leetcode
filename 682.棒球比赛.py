#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for val in ops:
            if val == '+':
                res.append(res[-2]+res[-1])
            elif val == 'D':
                res.append(res[-1]*2)
            elif val == 'C':
                res.pop()
            else:
                res.append(int(val))
        return sum(res)
    def calPoints(self, ops: List[str]) -> int:
        res = []
        total = 0
        for val in ops:
            if val == '+':
                res.append(res[-2]+res[-1])
                total += res[-1]
            elif val == 'D':
                res.append(res[-1]*2)
                total += res[-1]
            elif val == 'C':
                total -=res.pop()
            else:
                res.append(int(val))
                total += res[-1]
        return total
# @lc code=end

