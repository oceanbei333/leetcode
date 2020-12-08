#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换酒问题
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
             Bottles = numBottles//numExchange
             res += Bottles
             numBottles = numBottles%numExchange + Bottles
        return res
# @lc code=end

