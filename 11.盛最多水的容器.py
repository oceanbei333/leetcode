#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        length = len(height)
        for m in range(length):
            for n in range(m+1, length):
                max_area = max(max_area, min(height[m], height[n])*(n-m))
        return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        n = len(height) - 1
        max_area = 0
        while m < n:
            width = n - m
            if height[m] > height[n]:
                max_area = max(max_area, height[n]*width)
                n -= 1
            else:
                max_area = max(max_area, height[m]*width)
                m += 1
        return max_area


# @lc code=end
