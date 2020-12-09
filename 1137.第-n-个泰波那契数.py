#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        def _tribonacci(level:int, n1: int, n2:int, n3:int):
            if not level:
                return n1
            elif level == 1:
                return n2
            elif level == 2:
                return n3
            return _tribonacci(level-1, n2, n3, n1+n2+n3)
        return _tribonacci(n, 0,1,1)
        
# @lc code=end

