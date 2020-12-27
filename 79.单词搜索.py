#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        from collections import defaultdict

        def Trie():
            return defaultdict(Trie)
        root = tire = Trie()

        for c in word:
            root = root[c]
        root["is_word"] = True
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x: int, y: int, trie, visited: set) -> bool:
            if board[x][y] not in trie:
                return False
            trie = trie[board[x][y]]

            def check(i,j):
                if 0 <= i < m and 0 <= j < n and (i, j) not in visited and dfs(i, j, trie, visited | {(x, y)}):
                    return True

            if 'is_word' in trie:
                return True
            return any(check(x+di, y+dj) for di, dj in directions)

        return any(dfs(x, y, tire, set()) for x in range(m) for y in range(n))

    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x: int, y: int, k: int) -> bool:
            val = board[x][y]
            if val != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[x][y] = ''
            for di, dj in directions:
                i, j = x+di, y+dj
                if 0 <= i < m and 0 <= j < n and (i, j) and board[i][j] and dfs(i, j, k+1):
                    board[x][y] = val
                    return True
            board[x][y] = val
            return False

        return any(dfs(x, y, 0) for x in range(m) for y in range(n))


# @lc code=end
