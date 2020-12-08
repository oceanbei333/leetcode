#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin( x^y ).count('1')
    def hammingDistance(self, x: int, y: int) -> int:
        xory =x^y
        dis = 0
        while xory:
            if xory & 1:
                dis+=1
            xory >>= 1
        return dis
    def hammingDistance(self, x: int, y: int) -> int:
        xory =x^y
        dis = 0
        while xory:
            dis += 1
            xory &= (xory-1)
        return dis
        
# @lc code=end

