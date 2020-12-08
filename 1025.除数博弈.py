#
# @lc app=leetcode.cn id=1025 lang=python3
#
# [1025] 除数博弈
#

# @lc code=start
class Solution:
    def divisorGame(self, N: int) -> bool:
        return not N%2
        
    def divisorGame(self, N: int) -> bool:
        if N < 2:
            return False
        target = [False]*(N+1)
        target[2] = True
        for i in range(3, N+1):
            for j in range(1, i//2):
                if not i%j and not target[i-j]:
                    target[i] = True
        return target[N]
# @lc code=end

