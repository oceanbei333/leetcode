#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start

from typing import List, Tuple


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(end: int) -> int:
            if not end:
                return 1
            return max(dp(i)+1 if nums[end] > nums[i] else 1 for i in range(end))
        return max(dp(i) for i in range(len(nums)))

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        nums.append(float('-inf'))
        for i in range(n):
            dp[i] = max(dp[j]+1 for j in range(-1, i) if nums[i] > nums[j])
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        n = len(nums)
        if n < 2:
            return n
        res = 1
        # dp 每个长度的子序列中的末位置的最小值
        # dp是单调递增的
        dp = nums[0:1]
        for i in range(1, n):
            if nums[i] > dp[res-1]:
                dp.append(nums[i])
                res += 1
            else:
                # 更新之前的子序列的末位置的最小值
                dp[bisect.bisect_left(dp, nums[i])] = nums[i]
        return res

# @lc code=end
