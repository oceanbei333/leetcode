#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        adict = {val: i+1 for i, val in enumerate(arr2)}
        return sorted(arr1, key=lambda x:  adict.get(x) or x+len(arr2))

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        adict = {val: i-len(arr2) for i, val in enumerate(arr2)}
        return sorted(arr1, key=lambda x:  adict.get(x, x))

# @lc code=end
