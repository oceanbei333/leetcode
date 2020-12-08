#
# @lc app=leetcode.cn id=1266 lang=python3
#
# [1266] 访问所有点的最小时间
#

# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs( points[index][1]-points[index+1][1] ),abs( points[index][0]-points[index+1][0] )) for index in range(len(points)-1) )


        
# @lc code=end

