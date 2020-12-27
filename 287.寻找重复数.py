#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 1, n-1
        while l < r:
            mid = (l+r) >> 1
            count = sum(num <= mid for num in nums)
            if count <= mid:
                l = mid+1
            else:
                r = mid
        return r

    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        root = 0
        while root != slow:
            root = nums[root]
            slow = nums[slow]
        return slow


# @lc code=end
