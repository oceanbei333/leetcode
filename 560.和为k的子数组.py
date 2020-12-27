#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
from abc import abstractstaticmethod
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        pre = 0
        from collections import defaultdict
        adict = defaultdict(int)
        adict[0] = 1
        for i in range(n):
            pre += nums[i]
            if pre - k in adict:
                res += adict[pre-k]
            adict[pre] += 1
        return res


# @lc code=end
