#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        for val1, val2 in zip(heights, sorted(heights)):
            res += val1 !=val2
        return res
    def heightChecker(self, heights: List[int]) -> int:
        return sum( val1 != val2 for val1, val2 in zip(heights, sorted(heights)) )

# @lc code=end

