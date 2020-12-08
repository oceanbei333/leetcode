#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return sum(num*(num-1)//2 for num in counter.values())
# @lc code=end

