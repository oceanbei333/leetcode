#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        length = len(height)
        for l in range(length):
            for r in range(l+1, length):
                max_area = max(max_area, min(height[l], height[r])*(r-l))
        return max_area

    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            h = min(height[l], height[r])
            w = r-l
            max_area = max(max_area, h*w)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area


# @lc code=end
