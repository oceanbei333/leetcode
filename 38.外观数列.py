#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
from typing import Iterator


class Solution:
    @functools.lru_cache(None)
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        def get_next(s:str) -> str:
            result = ''
            count = 1
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count +=1
                else:
                    result += f"{count}{s[index-1]}"
                    count = 1
            result += f"{count}{s[-1]}"
            return result
        a_str = '1'
        for _ in range(n-1):
            a_str = get_next(a_str)
        return  a_str
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        def get_next(s:str) -> str:
            result = ''
            count = 1
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count +=1
                else:
                    result += f"{count}{s[index-1]}"
                    count = 1
            result += f"{count}{s[-1]}"
            return result
        return get_next(self.countAndSay(n-1))
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        def get_next(s:str) -> Iterator:
            count = 1
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count +=1
                else:
                    yield f"{count}{s[index-1]}"
                    count = 1
            yield f"{count}{s[-1]}"
        return ''.join(get_next(self.countAndSay(n-1)))

# @lc code=end

