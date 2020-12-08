#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#

# @lc code=start

from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        point1, point2, point3 = points
        return (point2[1]-point1[1])*(point3[0]-point2[0]) != (point3[1]-point2[1])*(point2[0]-point1[0])

        
# @lc code=end

