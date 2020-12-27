#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start

from typing import List, Optional, Union


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights = heights + [0]
        res = 0
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                res = max(res, heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        return res
# @lc code=end
