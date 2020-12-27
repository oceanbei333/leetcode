#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        right = [1]*n
        for i in range(1, n):
            left[i] = left[i-1]*nums[i-1]
            right[-i-1] = right[-i]*nums[-i]
        return [left[k]*right[k] for k in range(n)]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [1]*n
        for i in range(1, n):
            right[-i-1] = right[-i]*nums[-i]
        left = 1
        res = []
        for j in range(n):
            res.append(left*right[j])
            left *= nums[j]
        return res

# @lc code=end
