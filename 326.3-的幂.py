#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if not n:
            return False
        while not n%3:
            n //=3
        return n == 1
        
        
# @lc code=end

