#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter
        c = Counter(moves)
        return c['U']==c["D"] and c['R']==c['L']

        
# @lc code=end

