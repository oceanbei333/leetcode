#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(1)
        def dp(left:int, right:int)->int:
            if left == right:
                return 0
            result = []
            for i in range(left+1, right):
                result.append(dp(left,i)+dp(i, right)+ nums[i-1]*nums[i]*nums[i+1])
            return max(result) if result else 0
        return(dp(0, n-1))

        
# @lc code=end

