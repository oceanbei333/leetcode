#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#

# @lc code=start
from collections import Counter
from functools import reduce
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        return reduce(lambda x,y: x & y, map(Counter, A)).elements()

        
# @lc code=end

