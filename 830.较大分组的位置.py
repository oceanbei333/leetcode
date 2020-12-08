#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#

# @lc code=start
from typing import List
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        for index, val in enumerate(s):
            if not index:
                count = 1
                start = index
            else:
                if val ==pre:
                    count += 1
                else:
                    if count >2:
                        result.append([start, index-1])
                    count = 1
                    start = index
            pre = val
        if count > 2:
            result.append([start, index])
        return result


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        start = 0
        for index in range(len(s)):
            if index== len(s)-1 or s[index] != s[index+1]:
                if index - start >= 2:
                    result.append([start, index])
                start = index+1
        return result
# @lc code=end

