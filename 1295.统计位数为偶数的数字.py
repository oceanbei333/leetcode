#
# @lc app=leetcode.cn id=1295 lang=python3
#
# [1295] 统计位数为偶数的数字
#

# @lc code=start
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(not len(str(num))%2 for num in nums)
    def findNumbers(self, nums: List[int]) -> int:
        return sum(not int(math.log10(num)+1) %2  for num in nums)
# @lc code=end

