#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#

# @lc code=start
class Solution:
    def rotatedDigits(self, N: int) -> int:
        aset = set('0125689')
        bset = set('018')
        return sum(not(set(str(n)) - aset) and bool(set(str(n))-bset) for n in range(1, N+1))
# @lc code=end

