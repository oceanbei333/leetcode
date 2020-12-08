#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
from typing import List
from collections import OrderedDict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for index in range(len(nums)):
            wid_size = max(index-k, 0)
            for val in nums[wid_size: index]:
                if val == nums[index]:
                    return True
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k:
            return False
        adict = OrderedDict()
        for index in range(len(nums)):
            if nums[index] in adict:
                return True
            if index >= k:
                adict.pop(nums[index-k])
            adict[nums[index]] = 1
        return False


# @lc code=end
