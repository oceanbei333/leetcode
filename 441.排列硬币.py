#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if not n:
            return n
        from math import sqrt
        for i in range(1, int(sqrt(n*2)+1)+1):
            if i*(i+1)//2 == n:
                return i
            if i*(i+1)//2 > n:
                return i-1


        
# @lc code=end

