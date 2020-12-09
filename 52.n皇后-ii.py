#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0

        def dfs(cols: set, pie: set, na: set):
            row = len(cols)
            if row == n:
                self.count += 1
                return
            for col in range(n):
                if col not in cols and row+col not in pie and row-col not in na:
                    dfs(cols | {col}, pie | {row+col}, na | {row-col})
        dfs(set(), set(), set())
        return self.count

    def totalNQueens(self, n: int) -> int:
        def dfs(cols: int, pie: int, na: int):
            if bin(cols).count('1') == n:
                return 1
            bits = (~(cols | pie | na)) & ((1 << n)-1)
            res = 0
            while bits:
                p = bits & (-bits)
                bits = bits & (bits-1)
                res += dfs(cols | p, (pie | p) << 1, (na | p) >> 1)
            return res
        return dfs(0, 0, 0)
# @lc code=end
