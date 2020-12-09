#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        low =  float('inf')
        max_ = 0
        for p in prices:
            if p >= low:
                max_ = max(p-low, max_)
            else:
                low = p
        return max_
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        low = prices[0]
        max_ = 0
        for p in prices[1:]:
            if p >=low:
                max_ = max(p-low, max_)
            else:
                low = p
        return max_


# @lc code=end

