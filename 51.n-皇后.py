#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
from typing import List, Set, Tuple


class Solution:
    def solveNQueens(self, n: int) -> List[List]:
        res = []
        set_col = set()
        set_pie = set()
        set_na = set()

        def _solveNQueens(row: int, alist: List):
            if row == n:
                res.append(list(map(''.join, alist)))
                return
            for col in range(n):
                if (col not in set_col
                        and col+row not in set_pie
                        and row-col not in set_na
                    ):
                    alist[row][col] = 'Q'
                    set_col.add(col)
                    set_pie.add(col+row)
                    set_na.add(row-col)
                    _solveNQueens(row+1, alist)
                    alist[row][col] = '.'
                    set_col.remove(col)
                    set_pie.remove(col+row)
                    set_na.remove(row-col)
        alist = [['.']*n for _ in range(n)]
        _solveNQueens(0, alist)
        return res

    def solveNQueens(self, n: int) -> List[List]:

        def dfs(queue: List,  pie: set, na: set):
            row = len(queue)
            if row == n:
                res.append(queue)
                return
            for col in range(n):
                if not(col in queue or col+row in pie or row-col in na):
                    dfs(queue+[col], pie | {row+col}, na | {row-col})
        res = []
        dfs(list(), set(), set())
        return [['.'*col+'Q'+'.'*(n-1-col) for col in queue] for queue in res]

    def solveNQueens(self, n: int) -> List[List]:
        def dfs(queue: list,  col: int, pie: int, na: int):
            if len(queue) == n:
                res.append(queue)
                return
            bits = (~(col | pie | na)) & ((1 << n)-1)
            while bits:
                p = bits & -bits
                col_p = bin(p)[::-1].index('1')
                bits = bits & (bits-1)
                dfs(queue+[col_p],  col | p, (pie | p) << 1, (na | p) >> 1)
        res = []
        dfs(list(), 0, 0, 0)
        return [['.'*col+'Q'+'.'*(n-1-col) for col in queue] for queue in res]


# @lc code=end
