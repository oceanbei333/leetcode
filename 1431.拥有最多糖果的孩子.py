#
# @lc app=leetcode.cn id=1431 lang=python3
#
# [1431] 拥有最多糖果的孩子
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_n = max(candies)
        return list(map(lambda n: n+extraCandies>=max_n , candies))
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_n = max(candies)
        return [ n+extraCandies>=max_n for n in candies ]
# @lc code=end

