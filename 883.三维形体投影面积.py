#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

# @lc code=start
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        length = len(grid)
        bottom = length**2 - sum(nums.count(0) for nums in grid)
        area1 = sum(max(nums) for nums in grid)
        area2 = 0
        for i in range(length):
            area2 += max(grid[j][i] for j in range(length))
        return bottom + area1 + area2
    def projectionArea(self, grid: List[List[int]]) -> int:
        length = len(grid)
        res = 0
        for i in range(length):
            max1 = max2 = 0
            for j in range(length):
                res += bool(grid[i][j])
                max1 = max(max1, grid[i][j])
                max2 = max(max2, grid[j][i])
            res += max1+max2
        return res
    def projectionArea(self, grid: List[List[int]]) -> int:
        bottom = sum(len(grid) - nums.count(0) for nums in grid)
        area1 = sum(max(nums) for nums in grid)
        area2 = sum(max(nums)for nums in zip(*grid))
        return bottom + area1 +area2
        
# @lc code=end

