#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#

# @lc code=start
from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b_count = Counter("balloon")
        t_count = Counter(text) 
        res = 0
        while True:
            for s in b_count:
                if t_count[s] >= b_count[s]:
                    t_count[s] -= b_count[s]
                else:
                    return res
            res += 1

        
# @lc code=end

