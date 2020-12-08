#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        available = 0
        flowerbed.append(0)
        pre = 0
        for index in range(len(flowerbed)-1):
            if not pre and not flowerbed[index] and not flowerbed[index+1]:
                available += 1
                pre = 1
            else:
                pre = flowerbed[index]
            if available >= n:
                return True
        return False

# @lc code=end
