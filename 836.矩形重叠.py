#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#

# @lc code=start
from typing import List
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return (
            min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])
        and 
            min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])
        )
# @lc code=end

