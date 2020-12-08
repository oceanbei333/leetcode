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
        def is_vaild(s:str):
            stack = []
            for c in s:
                if c == '(':
                    stack.append(c)
                else:
                    if not stack:
                        return False
                    else:
                        stack.pop()
            return not stack
        res = []
        def _generateParenthesis(n:int, s:str):
            if not n:
                res.append(s)
                return
            _generateParenthesis(n-1, s+'(')
            _generateParenthesis(n-1, s+')')
        _generateParenthesis(n*2, '')
        return [c for c in res if is_vaild(c)]

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def _generateParenthesis(left:int, right:int, s:str):
            if right+left == 2*n:
                res.append(s)
            if left < n:
                _generateParenthesis(left+1, right, s+'(')
            if left > right and right < n:
                _generateParenthesis(left, right+1, s+')')
        _generateParenthesis(0, 0, '')
        return res

    def generateParenthesis(self, n: int) -> List[str]:
        @lru_cache(None)
        def _generateParenthesis(n:int):
            if not n:
                yield ''
            for i in range(n):
                for part_a in self.generateParenthesis(i):
                    for part_b in self.generateParenthesis(n-i-1):
                        #yield '(' + part_a +')' + part_b
                        yield f'({part_a}){part_b}'
        return list(_generateParenthesis(n))

            

            




# @lc code=end
