#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        target = total//k
        nums.sort()

        def dp(groups: List[int]):
            if not nums:
                return True
            num = nums.pop()
            for i in range(k):
                if groups[i] + num <= target:
                    groups[i] += num
                    if dp(groups):
                        return True
                    groups[i] -= num
                if not groups[i]:
                    break
            nums.append(num)
            return False
        return dp([0]*k)

# @lc code=end
