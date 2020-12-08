#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#

# @lc code=start
from typing import List
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        N = len(deck)
        for X in range(2, N+1):
            if not N%X:
                if all(not v%X for v in count.values()):
                    return True
        return False

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from fractions import gcd
        return reduce(gcd, collections.Counter(deck).values()) >= 2

# @lc code=end

