#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start

from typing import List, Tuple


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(len(nums))
        def dp(end: int) -> int:
            if not end:
                return 1
            return max(dp(i)+1 if nums[end] > nums[i] else 1 for i in range(end))
        return max(dp(i) for i in range(len(nums)))

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            dp[i] = max(dp[j]+1 if nums[i] > nums[j] else 1 for j in range(i))
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        # dp 每个长度的递增子序列中的的最小值
        # dp是单调递增的
        dp = nums[0:1]
        for i in range(1, len(nums)):
            index = bisect.bisect_left(dp, nums[i])
            if index >= len(dp):
                dp.append(nums[i])
            else:
                # 更新之前的子序列的最小值
                dp[index] = nums[i]
        return len(dp)



# @lc code=end
