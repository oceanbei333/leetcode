#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index in range(len(prices)-1):
            if prices[index+1] > prices[index]:
                profit += prices[index+1] - prices[index]
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        valley = peek = prices[0]
        index = 0
        length = len(prices)
        while index < length -1:
            while index< length-1 and prices[index] >= prices[index+1]:
                index += 1
            valley = prices[index]
            while index< length-1 and prices[index] <= prices[index+1]:
                index += 1
            peek = prices[index]
            profit += peek -valley
        return profit


# @lc code=end
