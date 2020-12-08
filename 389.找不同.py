#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        couter = Counter(t)
        couter.subtract(Counter(s))
        for c, n in couter.items():
            if n == 1:
                return c
    def findTheDifference(self, s: str, t: str) -> str:
        return (Counter(t) - Counter(s)).popitem()[0]
# @lc code=end

