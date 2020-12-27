#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

# @lc code=start
from typing import List


class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        length = [1]*l
        count = [1]*l
        for i in range(l):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[j] >= length[i]:
                        length[i] = length[j]+1
                        count[i] = count[j]
                    elif length[j]+1 == length[i]:
                        count[i] += count[j]
        longest = max(length)
        return sum(count[i] for i in range(l) if length[i] == longest)

# @lc code=end
