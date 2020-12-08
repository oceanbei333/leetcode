#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        @functools.lru_cache(26)
        def get_number(c: str)->int:
            return ord(c) -ord("A") + 1

        s = s[::-1]
        total = 0
        for index in range(len(s)):
            total += (26**index)*(get_number(s[index]) )
        return total

    def titleToNumber(self, s: str) -> int:
        @functools.lru_cache(26)
        def get_number(c: str)->int:
            return ord(c) -ord("A") + 1

        s = s[::-1]
        return sum((26**index)*(get_number(s[index]) ) for index in range(len(s)))
# @lc code=end

