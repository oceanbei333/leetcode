#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        t = 1
        while n:
            val = n%10
            s += val
            t *= val
            n //=10
        return t -s
        
# @lc code=end

