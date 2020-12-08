#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
from typing import List, Dict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        count: Dict[int, int] = dict()
        left: Dict[int, int] = dict()
        right: Dict[int, int] = dict()
        for index, val in enumerate(nums):
            if val not in count:
                left[val] = index
            count[val] = count.get(val, 0) + 1
            right[val] = index
        degree = max(count.values())
        ans = len(nums)
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x]-left[x]+1)
        return ans


# @lc code=end
