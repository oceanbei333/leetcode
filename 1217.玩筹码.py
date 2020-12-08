#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 玩筹码
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(sum(1 for num in position if not num%2),sum(1 for num in position if num%2))
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_n = 0
        even_n = 0
        from collections import defaultdict
        adict = defaultdict(int)
        for num in position:
            if num%2:
                odd_n += 1
            else:
                even_n += 1
        return min(odd_n, even_n)


# @lc code=end

