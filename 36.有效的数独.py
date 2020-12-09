#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        block = [[set() for _ in range(3)] for _ in range(3)]
        for x in range(9):
            for y in range(9):
                num = board[x][y]
                if num == '.':
                    continue
                if num in row[x] or num in col[y] or num in block[x//3][y//3]:
                    return False
                row[x].add(num)
                col[y].add(num)
                block[x//3][y//3].add(num)
        return True


# @lc code=end
