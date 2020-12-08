#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        v_max = max(A)
        v_min = min(A)
        return max( v_max - v_min- 2*K , 0)
        
# @lc code=end

