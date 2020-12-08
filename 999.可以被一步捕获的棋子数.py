#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 可以被一步捕获的棋子数
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        res = 0
        for row in board:
            pre = row[0]
            for val in row[1:]:
                if val == 'R' and pre == 'p' or val == 'p' and pre == 'R':
                    res += 1
                if val in {'R', 'p', 'B'}:
                    pre = val
        for row in zip(*board ):
            pre = row[0]
            for val in row[1:]:
                if val == 'R' and pre == 'p' or val == 'p' and pre == 'R':
                    res += 1
                if val in {'R', 'p', 'B'}:
                    pre = val
        return res
    def numRookCaptures(self, board: List[List[str]]) -> int:
        self.res = 0
        def check(row):
            pre = row[0]
            for val in row[1:]:
                if val == 'R' and pre == 'p' or val == 'p' and pre == 'R':
                    self.res += 1
                if val in {'R', 'p', 'B'}:
                    pre = val
        tuple(map(check, board))
        tuple(map(check, zip(*board)))
        return self.res
                

# @lc code=end

