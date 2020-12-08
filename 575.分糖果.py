#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        aset = set()
        half = len(candies)//2
        for val in candies:
            if len(aset) >= half:
                break
            if val not in aset:
                aset.add(val)
        return len(aset)
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(candies )//2, len(set(candies)))

# @lc code=end

