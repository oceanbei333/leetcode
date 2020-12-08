#
# @lc app=leetcode.cn id=1560 lang=python3
#
# [1560] 圆形赛道上经过次数最多的扇区
#

# @lc code=start
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        if rounds[-1] >= rounds[0]:
            return list(range(rounds[0], rounds[-1]+1))
        else:
            return list(range(1, rounds[-1]+1)) + list(range(rounds[0], n+1))
# @lc code=end

