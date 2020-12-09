#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def Trie(): return defaultdict(Trie)
        row = len(board)
        col = len(board[0])

        trie = Trie()
        for word in words:
            root = trie
            for c in word:
                root = root[c]
            root['word'] = word
        res = []

        def dfs(x, y, trie):
            if x < 0 or x >= row or y < 0 or y >= col:
                return
            tmp = board[x][y]
            if not tmp or tmp not in trie:
                return
            cur = trie[board[x][y]]
            # check found a word
            word = cur.pop('word', False)
            if word:
                res.append(word)
            # remove the word in the trie if it is last char
            if not cur:
                trie.pop(tmp)
                return
            board[x][y] = ''
            for m, n in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
                dfs(m, n, cur)
            board[x][y] = tmp
        for x in range(row):
            for y in range(col):
                dfs(x, y, trie)
        return res

# @lc code=end
