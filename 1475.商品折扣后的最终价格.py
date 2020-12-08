#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j]<=prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices

    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for index in range(len(prices)):
            while stack and prices[ stack[-1] ] >= prices[index]:
                prices[stack.pop()] -= prices[index]
            stack.append(index)
        return prices
# @lc code=end

