#
# @lc app=leetcode.cn id=1346 lang=python3
#
# [1346] 检查整数及其两倍数是否存在
#

# @lc code=start
from typing import Collection


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        if counter[ 0 ] > 1:
            return True
        return any(counter[ num*2 ] for num in counter if num)
    def checkIfExist(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        if counter[0] > 1:
            return True
        aset = set(arr)
        return any(2*num in aset for num in aset if num)
       
# @lc code=end

