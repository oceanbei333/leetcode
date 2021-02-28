#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution:
    def minSteps(self, n):
        ans = 0
        d = 2
        while n > 1:
            while not n % d :
                ans += d
                n /= d
            d += 1
        return ans
        
# @lc code=end

