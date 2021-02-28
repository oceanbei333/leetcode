#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List, Generator

from typing import List
from functools import lru_cache


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(left: int, right: int, s: str):
            if right+left == 2*n:
                res.append(s)
            else:
                if left < n:
                    helper(left+1, right, s+'(')
                if left > right and right < n:
                    helper(left, right+1, s+')')
        helper(0, 0, '')
        return res

    def generateParenthesis(self, n: int) -> List[str]:
        @lru_cache(n)
        def helper(n: int):
            if not n:
                return ['']
            res = []
            for i in range(n):
                for part_a in helper(i):
                    for part_b in helper(n-i-1):
                        res.append(f'({part_a}){part_b}')
            return res
        return helper(n)

    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for i in range(n+1)]
        dp[0].append('')
        dp[1].append('()')
        for i in range(2, n+1):
            dp[i] = [
                f'({part_a}){part_b}'
                for j in range(i)
                for part_a in dp[j]
                for part_b in dp[i-1-j]
            ]
        return dp[n]


# @lc code=end
