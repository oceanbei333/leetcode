#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#

# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s = sum(distance)
        if destination < start:
            destination, start = start, destination
        d1 = sum(distance[start:destination])
        return min(d1, s-d1)
        
# @lc code=end

