#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n<2:
            return []
        res= []
        def helper(used:List[int], index:int):
            print(used)
            if index >=n:
                if len(used)>=3:
                    res.append(used[1:])
                return
            for i in range(index,n):
                if i !=index and nums[i]==nums[i-1]:
                    continue
                if used[-1]<nums[i]:
                    helper(used+[nums[i]], index+1)
                helper(used[:],index+1)
        helper([float('-inf')], 0)
        return res
# @lc code=end

