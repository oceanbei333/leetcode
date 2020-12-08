#
# @lc app=leetcode.cn id=1033 lang=python3
#
# [1033] 移动石子直到连续
#

# @lc code=start
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a,b,c])
        ab = b-a
        bc = c-b
        if ab==bc==1:
            min_m = 0
        elif ab <3 or bc <3:
            min_m = 1
        else:
            min_m = 2
        max_m = c-b+b-a-2
        return min_m, max_m

        
# @lc code=end

