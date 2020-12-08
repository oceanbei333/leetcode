#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        @functools.lru_cache(26)
        def get_char(n:int)->str:
            return chr(ord('A')+n)
        res = ''
        while n:
            n -= 1
            res = get_char((n)%26) + res
            n //= 26 
        return res

        
# @lc code=end

