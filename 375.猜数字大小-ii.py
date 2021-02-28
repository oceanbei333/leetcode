#
# @lc app=leetcode.cn id=375 lang=python3
#
# [375] 猜数字大小 II
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dp(l, r):
            if r-l == 2:
                return l
            if r-l <= 1:
                return 0
            return min((i+max(dp(l, i), dp(i+1, r)) for i in range(l, r)))
        return dp(1, n+1)
# @lc code=end
