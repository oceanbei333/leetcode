#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        res = n+1
        for i in range(n):
            total = 0
            for length in range(1, n+1):
                if i + length-1 < n:
                    total += nums[i+length-1]
                    if total >= s:
                        res = min(res, length)
                        break
        return res if res < n+1 else 0

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        sums = [0]
        for i in range(n):
            sums.append(sums[-1]+nums[i])

        res = n+1
        for i in range(n):
            target = s+sums[i]
            from bisect import bisect_left
            index = bisect_left(sums, target)
            if index != n+1:
                res = min(res, index-i)

        return res if res != n+1 else 0

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        res = n+1
        total = 0
        while r < n:
            total += nums[r]
            while total >= s:
                res = min(res, r-l+1)
                total -= nums[l]
                l += 1
            r += 1
        return res if res != n+1 else 0


# @lc code=end
