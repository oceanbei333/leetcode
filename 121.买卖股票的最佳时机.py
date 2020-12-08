#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_price = float('-inf')
        max_profit = 0
        for val in prices1:
            if val > low_price:
                max_profit = max(val-low_price, max_profit)
            else:
                low_price = val
        return max_profit
            


# @lc code=end

