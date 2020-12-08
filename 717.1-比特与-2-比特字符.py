#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1比特与2比特字符
#

# @lc code=start
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        parity = bits.pop()
        while bits and bits.pop():
            parity ^= 1
        return parity == 0


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            i += bits[i]+1
        return i == len(bits)-1

# @lc code=end
