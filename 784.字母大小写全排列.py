#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        visited = set()

        def dfs(word: str):
            if word in visited:
                return
            visited.add(word)
            for i in range(len(word)):
                if word[i].islower():
                    dfs(word[:i]+word[i].upper()+word[i+1:])
                if word[i].isupper():
                    dfs(word[:i]+word[i].lower()+word[i+1:])
        dfs(S)
        return list(visited)

    def letterCasePermutation(self, S: str) -> List[str]:
        res = [[]]
        for char in S:
            n = len(res)
            if char.isalpha():
                for i in range(n):
                    res.append(res[i].copy())
                    res[i].append(char.lower())
                    res[i+n].append(char.upper())
            else:
                for i in range(n):
                    res[i].append(char)
        return [''.join(alist) for alist in res]

    def letterCasePermutation(self, S: str) -> List[str]:
        B = sum(char.isalpha() for char in S)
        res = []
        for bits in range(1 << B):
            word = ''
            for char in S:
                if char.isalpha():
                    if bits & 1:
                        word += char.lower()
                    else:
                        word += char.upper()
                    bits >>= 1
                else:
                    word += char
            res.append(word)
        return res

    def letterCasePermutation(self, S: str) -> List[str]:
        def f(x):
            return (x.lower(), x.upper()) if x.isalpha() else x
        from itertools import product
        return list(map("".join, product(*map(f, S))))


# @lc code=end
