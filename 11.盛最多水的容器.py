#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                res = max((j-i)*min(height[i], height[j]), res)
        return res
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        res = 0
        while i<j:
            length = j-i
            if height[i] >= height[j]:
                h = height[j]
                j-=1
            else:
                h = height[i]
                i+=1
            res = max(h*length, res)
        return res
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        res = 0
        while i<j:
            res = max(min(height[i], height[j])*(j-i), res)
            if height[i] >= height[j]:
                j-=1
            else:
                i+=1
        return res

# @lc code=end

