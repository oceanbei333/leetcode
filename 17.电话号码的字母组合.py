#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List, Tuple


class Solution:
    def get_letters(self, num:int)->str:
        res = ''
        if num <7:
            for i in range((num-2)*3, (num-1)*3):
                res += chr(ord('a')+i)
        elif num == 7:
            res += 'pqrs'
        elif num == 8:
            res += 'tuv'
        else:
            res += 'wxyz'
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        def _letterCombinations(index, s:str):
            if index == len(digits):
                res.append(s)
                return
            letters = self.get_letters(int(digits[index]))
            for lettter in letters:
                _letterCombinations(index+1, s+lettter)
        _letterCombinations(0, '')
        return res
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = ['']
        for num in digits:
            letters = self.get_letters(int(num))
            alist = []
            for letter in letters:
                for s in res:
                    alist.append(s+letter)
            res = alist
        return res
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = ['']
        for num in digits:
            letters = self.get_letters(int(num))
            res = [s+letter for letter in letters for s in res]
        return res

# @lc code=end

